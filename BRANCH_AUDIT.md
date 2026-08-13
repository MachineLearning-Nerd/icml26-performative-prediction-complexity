# Branch audit

## Canonical surface

`main` is the canonical publication branch. The historical branches
below were development snapshots and have been consolidated into `main`.

| Historical branch | Role |
| --- | --- |
| `orx/baseline-env-setup` | Initial environment and weak source-pinned verifier. |
| `orx/rigorous-claim-verification` | Added rigorous per-claim verifier logic. |
| `orx/rigorous-verification-final` | Final rigorous verification snapshot. |
| `orx/rigorous-verification-hf` | Public/Hugging Face handoff mirror of the rigorous snapshot. |

These branches are lineage only. Their raw `VERIFIED` language describes
the finite producer contracts, not independent proof of the paper’s theorems.

## Publication-time checks

Checked on 2026-08-13:

- Repository target: `icml26-performative-prediction-complexity`.
- Default and only remote branch after cleanup: `main`.
- Maintainer identity: MachineLearning-Nerd.
- Paper source: arXiv:2601.20180v1, OpenReview: kkhVljGiMS.
- Consolidated result: 6/6 finite contracts pass; 0/6 paper claims independently
  verified; overall INCONCLUSIVE.
