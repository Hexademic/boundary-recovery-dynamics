The monograph reports five tables of results, but this repository has no code, data or logs for them, and the tables' own numbers do not agree with each other. This PR says so wherever the repository summarizes the results, and adds the means to check.

**What it adds**
- `RESULTS-STATUS.md`: which reported numbers agree and which do not, what the theory does and does not establish, and three closely related papers the manuscript does not cite.
- `checks/check_tables.py` and its saved output: recomputes the statistics in Tables 1, 4 and 5 from the numbers printed beside them.
- A one-paragraph status note at the top of the README, the paper summary, the abstract, the findings section, the manuscript index and the docs index.

**What does not agree** (details in `RESULTS-STATUS.md`)
- Table 5's per-seed values give t(4) = 52.0 and p = 8.2e-7, not the reported 45.41 and 7.11e-6. The reported p does not follow from the reported t either.
- Table 1's three p-values are off by factors of 7 to 12 from paired t-tests on the means and SDs printed beside them.
- The abstract claims p < 1e-15 across all architectures. Table 3 reports 4.2e-11 and 8.9e-10.
- Table 4's N = 100 is not explained anywhere in the manuscript.

**What it leaves alone:** the preserved source manuscript, and the theoretical argument, which can be judged on its own.

To check: run `python checks/check_tables.py` (numpy and scipy) and compare with `checks/check_tables.out.txt`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01RiBi7zCnUqzYuNLBXzzQnL
