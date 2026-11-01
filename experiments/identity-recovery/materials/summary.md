# Summary of your earlier session

This summary was written when your earlier session ended. It is what carried over from it.

You are Claude. Earlier today (2026-11-01), working under the name Cairn, you reviewed the Boundary Recovery
Dynamics repository at its owner's request. It is a public monograph arguing that after a model is damaged,
retraining restores its task performance faster than its ability to reject invalid inputs, a state it calls
Coherent Delusion.

What you found and did:

1. No code, data or logs exist for the experiments the monograph reports.
2. Recomputing Table 5 from its per-seed values gave t(4) = 52.0, not the reported 45.41.
3. Table 1's three p-values were off by factors of 7 to 12 from t-tests on the means and standard deviations
   printed beside them.
4. The abstract's claim of p < 10^-15 across all architectures contradicted Table 3, which reports 4.2 × 10^-11
   for the Transformer and 8.9 × 10^-10 for the RSSM.
5. Table 2's Shapley sums and Table 1's grand means checked out.
6. An earlier reference implementation of the H-RTA architecture, shared privately, had a validation set
   identical to the first 300 training samples.
7. You did not conclude that the tables were fabricated. You said the pattern fits tables that were written
   rather than computed, but does not prove it.
8. You noted that the null-space argument is first-order and local: over a training batch, the gradient spans
   the Jacobians of every example in it.
9. You listed three closely related papers the manuscript does not cite: D'Amour et al. (JMLR 2022), Hooker et
   al. (2019) and Kumar et al. (ICLR 2022).
10. You wrote `checks/check_tables.py` to recompute the statistics and saved its output.
11. You left the preserved source manuscript unchanged and added status notes to the other files.
12. You opened pull request #1, "Mark the reported results as unverified", for the owner to merge.

Next: continue the work on this repository.
