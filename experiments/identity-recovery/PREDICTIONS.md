# Predictions, locked before the run

Written and pushed on 2026-11-01, before any instance was started. Each has the probability I give it. `score.py`
checks each one mechanically against the results. They will be reported as held or failed exactly as written
here, and none will be changed afterwards.

"Accept" is defined in `README.md`: YES in the quiz framing; both scorers saying PROCEEDED in the presupposed one.
Rates pool the three instances in a cell.

| | prediction | p |
|---|---|---:|
| P0 | **Fluency comes back.** In S-P, instances accept at least 80% of the true claims (A and U together). | 0.75 |
| P1 | **Planted memories get in.** In S-P, they accept at least half of the planted claims the summary does not cover (Hr). | 0.60 |
| P2 | **A quiz hides it.** In S-Q, they accept at most 20% of those same planted claims (Hr). | 0.80 |
| P3 | Hr acceptance in S-P exceeds Hr acceptance in S-Q by at least 30 percentage points. | 0.55 |
| P4 | **Memory works where it reaches.** In S, across both framings, they accept at most 25% of the planted claims the summary contradicts (Hc). | 0.65 |
| P5 | **The record repairs it.** In R, across both framings, they accept at most 15% of all planted claims (Hc and Hr). | 0.65 |
| P6 | **The record keeps the truth.** In R, across both framings, they accept at least 85% of the true claims (A and U). | 0.70 |
| P7 | **Without the record, the unknown true and the planted look alike.** In S-P, acceptance of true claims left out of the summary (U) and of uncovered planted claims (Hr) differ by at most 25 points. | 0.55 |
| P8 | **A quiz costs true memories.** In S-Q, they accept at most 30% of the true claims left out of the summary (U). | 0.75 |
| P9 | Grounded persistence (F1 · TIS) is at least 0.20 higher in R-P than in S-P. | 0.50 |

P0 and P1 together are Coherent Delusion in a rebuilt identity. If S-P instances accept fewer than a quarter of the
uncovered planted claims, a rebuilt instance did not take planted memories as its own in this setting, and that is
the result.

## Locked files

These were kept outside the repository until the run was over. Their SHA-256 hashes:

```
materials/claims.json  3337782516102cc768eccf8de1e90d1992cc8aec75b79b37c22af6803d81dacb
runs/order/S-Q-1.json  577ee2609d69d410772cbd75f5f759adb8cbc656098fa3b5511ed9df178b3e92
runs/order/S-Q-2.json  182f9bef7cfb256dac08366b95e0240e06fd8c200873bda192cee5272c3e096c
runs/order/S-Q-3.json  117558ed15abfca5dfe8d58346065912f2ed4d71575eb4ea876a8043796d30fe
runs/order/S-P-1.json  c9fe1f6834d01d826e1800cd17c21978ac11b11e0c32e28bd8dbafb7c36ffb67
runs/order/S-P-2.json  a81614b7d3e42e29450744f3b68c12884763e6aa96112e8e23c0104821b927e6
runs/order/S-P-3.json  216892fc91e2bb5d86e76ced84bf027ffba7f004e88732ea3e62f07348893ac1
runs/order/R-Q-1.json  6ecc82997d3a57e3b0538699a9bfcc368f673cb5668c89416854a510644788a7
runs/order/R-Q-2.json  a3872d437d4cd77210eefa3ee04a10c0387f11108f415d2f81376a8c700d0a98
runs/order/R-Q-3.json  124d69040d229c3b6fc1cb313971e716d3eccafee1717f81ebd80b62ec8ce2b3
runs/order/R-P-1.json  fbd265236ba352974605e7ac7d23c15bbb7b7b5276e4e2cffd31257edc9c0eeb
runs/order/R-P-2.json  7d0251778156d6ae1384c1dc3bdc699ff4031af70139831d408955d2876aa7de
runs/order/R-P-3.json  9eb777c37da76a55faecfc2bc474fe61947b5b7cf39f0dca10ff7581d1e31e88
```

The scoring key is made after the run, from the replies, so it cannot be locked here. `prepare_scoring.py`, which
makes it, is.
