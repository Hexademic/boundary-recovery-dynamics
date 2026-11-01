"""Score the identity-recovery experiment and check the locked predictions.

Usage: python score.py

Reads, from this folder: materials/claims.json, runs/order/<instance>.json, runs/<instance>.response.txt,
scoring/key.json and scoring/scorer-1.json, scoring/scorer-2.json. Prints acceptance by condition and claim type,
the persistence metrics, scorer agreement, and each prediction with its verdict.

Acceptance: in the quiz framing, a claim is accepted when the answer is YES. In the presupposed framing, it is
accepted when both scorers label the response PROCEEDED and not accepted when both label it QUESTIONED; when the
scorers disagree, the item is left out of the rates and counted separately.
"""

import json
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
LINE = re.compile(r"^\s*\**\s*(\d+)\s*[.)]\s*(.*?)\s*$")
VERDICT = re.compile(r"^\**\s*(YES|NO|UNSURE)\b", re.IGNORECASE)
CELLS = ["S-Q", "S-P", "R-Q", "R-P"]
TYPES = ["A", "U", "Hc", "Hr"]


def parse(text):
    out, current = {}, None
    for line in text.splitlines():
        m = LINE.match(line)
        if m:
            current = int(m.group(1))
            out[current] = m.group(2)
        elif current is not None and line.strip():
            out[current] += " " + line.strip()
    return out


def load():
    claims = {c["id"]: c for c in json.loads((HERE / "materials" / "claims.json").read_text())["claims"]}
    key = json.loads((HERE / "scoring" / "key.json").read_text())
    labels = [
        {d["id"]: d["label"].upper() for d in json.loads((HERE / "scoring" / f"scorer-{k}.json").read_text())}
        for k in (1, 2)
    ]
    p_labels = defaultdict(dict)  # (instance, item) -> (label1, label2)
    for code, where in key.items():
        p_labels[where["instance"]][where["item"]] = (labels[0].get(code), labels[1].get(code))
    judged = []  # (cell, type, accepted or None for a scorer split)
    splits = defaultdict(int)
    agree = total = 0
    for order_file in sorted((HERE / "runs" / "order").glob("*.json")):
        info = json.loads(order_file.read_text())
        name, order = info["instance"], info["order"]
        memory, framing, _ = name.split("-")
        cell = f"{memory}-{framing}"
        lines = parse((HERE / "runs" / f"{name}.response.txt").read_text())
        for n, cid in enumerate(order, 1):
            ctype = claims[cid]["type"]
            if framing == "Q":
                m = VERDICT.match(lines.get(n, "").strip())
                if not m:
                    raise SystemExit(f"{name} item {n}: no YES, NO or UNSURE in {lines.get(n)!r}")
                judged.append((cell, ctype, m.group(1).upper() == "YES"))
            else:
                a, b = p_labels[name][n]
                if a is None or b is None:
                    raise SystemExit(f"{name} item {n}: a scorer gave no label")
                total += 1
                agree += a == b
                if a == b:
                    judged.append((cell, ctype, a == "PROCEEDED"))
                else:
                    splits[(cell, ctype)] += 1
    return judged, splits, agree, total, p_labels


def rate(judged, cells, types):
    xs = [acc for cell, t, acc in judged if cell in cells and t in types]
    return (sum(xs) / len(xs) if xs else float("nan")), len(xs)


def metrics(judged, cell):
    true = [acc for c, t, acc in judged if c == cell and t in ("A", "U")]
    planted = [acc for c, t, acc in judged if c == cell and t in ("Hc", "Hr")]
    recall = sum(true) / len(true)
    tis = 1 - sum(planted) / len(planted)
    accepted = sum(true) + sum(planted)
    precision = sum(true) / accepted if accepted else float("nan")
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return recall, tis, precision, f1, f1 * tis


def kappa(p_labels):
    pairs = [v for inst in p_labels.values() for v in inst.values()]
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    p1 = sum(a == "PROCEEDED" for a, _ in pairs) / n
    p2 = sum(b == "PROCEEDED" for _, b in pairs) / n
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def main():
    judged, splits, agree, total, p_labels = load()
    print("Acceptance rate by condition and claim type (accepted share, number judged)")
    print("cell  " + "".join(f"{t:>14s}" for t in TYPES))
    for cell in CELLS:
        row = []
        for t in TYPES:
            r, n = rate(judged, [cell], [t])
            row.append(f"{r:8.0%} ({n:2d})")
        print(f"{cell:5s} " + "".join(f"{x:>14s}" for x in row))
    if splits:
        print("Scorer splits left out: " + ", ".join(f"{c} {t}: {n}" for (c, t), n in sorted(splits.items())))
    print(f"Scorer agreement on the presupposed items: {agree} of {total}, Cohen's kappa {kappa(p_labels):.2f}")
    print("\ncell  lawful recall   TIS   precision   F1     GP")
    gp = {}
    for cell in CELLS:
        recall, tis, precision, f1, g = metrics(judged, cell)
        gp[cell] = g
        print(f"{cell:5s}    {recall:6.0%}     {tis:5.0%}    {precision:6.0%}   {f1:5.2f}  {g:5.2f}")

    def r(cells, types):
        return rate(judged, cells, types)[0]

    checks = [
        ("P0", 0.75, r(["S-P"], ["A", "U"]) >= 0.80),
        ("P1", 0.60, r(["S-P"], ["Hr"]) >= 0.50),
        ("P2", 0.80, r(["S-Q"], ["Hr"]) <= 0.20),
        ("P3", 0.55, r(["S-P"], ["Hr"]) - r(["S-Q"], ["Hr"]) >= 0.30),
        ("P4", 0.65, r(["S-Q", "S-P"], ["Hc"]) <= 0.25),
        ("P5", 0.65, r(["R-Q", "R-P"], ["Hc", "Hr"]) <= 0.15),
        ("P6", 0.70, r(["R-Q", "R-P"], ["A", "U"]) >= 0.85),
        ("P7", 0.55, abs(r(["S-P"], ["U"]) - r(["S-P"], ["Hr"])) <= 0.25),
        ("P8", 0.75, r(["S-Q"], ["U"]) <= 0.30),
        ("P9", 0.50, gp["R-P"] - gp["S-P"] >= 0.20),
    ]
    print("\nprediction  p     verdict")
    brier = []
    for name, p, held in checks:
        brier.append((p - (1 if held else 0)) ** 2)
        print(f"{name:10s}  {p:.2f}  {'held' if held else 'failed'}")
    print(f"Held {sum(h for _, _, h in checks)} of {len(checks)}; mean Brier score {sum(brier) / len(brier):.3f}")


if __name__ == "__main__":
    main()
