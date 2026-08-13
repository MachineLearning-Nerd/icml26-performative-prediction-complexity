---
title: "ICML 2026 — Computational Complexity of Performative Prediction"
emoji: "⚖️"
colorFrom: blue
colorTo: purple
sdk: static
pinned: false
tags:
  - icml2026-repro
  - paper-kkhVljGiMS
  - source-pinned
  - finite-audit
---

# ICML 2026 — Computational Complexity of Performative Prediction

Independent, CPU-only, source-pinned finite audit for:

> Ioannis Anagnostides, Rohan Chauhan, Ioannis Panageas, Tuomas Sandholm, and
> Jingming Yan. “On the Computational Complexity of Performative Prediction.”
> [arXiv:2601.20180v1](https://arxiv.org/abs/2601.20180).
> OpenReview: [kkhVljGiMS](https://openreview.net/forum?id=kkhVljGiMS).

Repository name: `icml26-performative-prediction-complexity`

## Current status

**Overall: INCONCLUSIVE.** Six finite source/formula contracts pass. The
repository does not independently prove PPAD-completeness, PLS-hardness,
tractability over all inputs, query lower bounds, or the paper’s other
complexity-theoretic quantifiers.

| Layer | Result | Meaning |
| --- | --- | --- |
| Finite contract checks | 6/6 pass | Source anchors, selected finite algebraic/scaling controls, local objective checks, and negative controls pass. |
| Paper-level claims | 0/6 independently verified | Finite source checks do not establish reductions, hardness transfers, algorithms over all instances, or asymptotic complexity bounds. |
| Consolidated status | INCONCLUSIVE | This is finite audit evidence, not a proof of the paper’s theorems. |

The raw `outputs/verification.json` uses `verified` for the
producer contracts. In that file it means that the declared finite contract
passed. The consolidated gate in `publication_gate.json` reports
`FINITE_CONTRACT_PASS` separately from the paper-level status.

The local paper archive is pinned to SHA-256
`c32199596640624de68ae92f19d4db2324d837580da51db25910213388262b76`.
The public arXiv record currently has only v1.

## What the paper does

The paper studies the computational complexity of finding performatively stable
points when a deployed model changes the data distribution. It identifies a
phase transition near the repeated-risk-minimization boundary: PPAD-hardness
persists in simple quadratic/linear settings, a narrow regime admits a
tractability result, and further results cover query lower bounds, general
convex domains, and strategic classification with PLS-hardness.

This repository audits selected source expressions and finite controls related
to those six claims. It should not be described as a complete reduction
reproduction.

## Claim ledger: producer → check → boundary

All six claims are produced by
`repro/src/verify_performative_complexity.py`. The publication runner
`repro/src/run_publication_gate.py` runs that verifier and the
standard-library regression test. The explanatory notebook
`notebooks/performative_complexity.py` contains demonstrations, but it
is not the consolidated verifier.

| Claim | Paper object | What the committed verifier checks | Boundary |
| --- | --- | --- | --- |
| C1 | Theorem 3.4 PPAD-completeness threshold | Confirms source anchors and four finite `epsilon`/`rho` threshold relationships using `epsilon'=0.088/6`; rejects a wrong denominator. | Does not implement the affine-VI reduction or prove PPAD-hardness. |
| C2 | Quadratic loss and affine distribution shift | Confirms the source anchor and four affine fixed-point residual cells; rejects a perturbed fixed point. | Does not establish the complete quadratic/affine hardness reduction. |
| C3 | Theorem 3.5 tractability window | Confirms the `poly(d, log(1/epsilon))` source anchor and four monotone `epsilon^4` scaling cells. | Does not prove an ellipsoid algorithm or worst-case complexity over all inputs. |
| C4 | Corollary 3.7 query lower bound | Confirms the `2^{Omega(d)}` source anchor and 12 finite monotone query-scale values. | Does not implement the HPS hiding game or prove the lower bound. |
| C5 | Theorem 3.12 convex-domain hardness | Confirms the `well-bounded` source anchor in the pinned convex-domain source. | No committed Sperner reduction or universal convex-domain hardness proof. |
| C6 | Theorem 4.4 strategic-classification PLS-hardness | Confirms the `PLS-hard` source anchor and one finite strict-local-objective control. | No committed local-max-cut reduction or proof of PLS-hardness. |

A contract passes only when its source anchors and declared finite checks pass and
its negative controls behave as expected. Passing a contract is not the same as
verifying the associated theorem.

## Reproduce

The project uses Python 3.11+ with dependencies pinned by `uv.lock`:

```bash
uv sync --frozen
uv run python repro/src/run_publication_gate.py
```

For a lightweight consolidated summary from the existing raw output:

```bash
uv run python repro/src/finalize_gate.py
```

The full runner regenerates `outputs/verification.json`, runs the
regression test, and writes the raw gate. It does not turn finite checks into
complexity-theoretic proofs.

## Limitations

- Source-token checks confirm that the cited objects exist in the pinned archive;
  they do not validate every displayed derivation.
- Finite threshold, scale, affine, and local-objective cells cannot establish
  universal reductions, PPAD/PLS hardness, or polynomial/exponential worst-case
  complexity.
- The notebook includes simplified demonstrations, including an ellipsoid-style
  example; these are explanatory and are not paper-level verification.
- The audit relies on cited prior hardness results and does not re-prove them.
- No author executable release or empirical benchmark is claimed by this
  repository; the paper is theoretical and this bundle is a finite audit.
- No GPU or paid compute is required.

## Branches

`main` is the canonical publication branch. Historical branches are
documented so their roles remain clear:

| Branch | Role |
| --- | --- |
| `orx/baseline-env-setup` | Initial environment and weak source-pinned verifier. |
| `orx/rigorous-claim-verification` | Added the rigorous per-claim verifier implementation. |
| `orx/rigorous-verification-final` | Final rigorous verification snapshot; same tip as the HF handoff branch. |
| `orx/rigorous-verification-hf` | Hugging Face/publication handoff mirror of the rigorous snapshot. |

These branches were development lineage, not separate scientific results. The
cleaned remote retains only `main`; see
[BRANCH_AUDIT.md](BRANCH_AUDIT.md).

## Repository map

- `repro/src/verify_performative_complexity.py`: source-pinned finite producer.
- `repro/src/run_publication_gate.py`: full finite gate runner.
- `repro/src/finalize_gate.py`: consolidated finite-vs-paper gate.
- `repro/tests/`: regression test.
- `notebooks/performative_complexity.py`: explanatory interactive notebook.
- `reports/`: detailed audit narrative.
- `source/`: pinned arXiv source archive.
- `outputs/`: raw verification and gate JSON.
- `STATUS.md`, `GATE_READY.md`, and
  `BRANCH_AUDIT.md`: status, gate, and branch lineage.

## Citation

```bibtex
@article{anagnostides2026computational,
  title   = {On the Computational Complexity of Performative Prediction},
  author  = {Anagnostides, Ioannis and Chauhan, Rohan and Panageas, Ioannis and Sandholm, Tuomas and Yan, Jingming},
  journal = {arXiv preprint arXiv:2601.20180},
  year    = {2026},
  url     = {https://arxiv.org/abs/2601.20180}
}
```

## Thank you and attribution

Thank you to Ioannis Anagnostides, Rohan Chauhan, Ioannis Panageas, Tuomas
Sandholm, and Jingming Yan for making this theoretical work available for
careful study. This repository is an independent finite audit, not an official
implementation or endorsement by the authors.

Maintained by [MachineLearning-Nerd](https://github.com/MachineLearning-Nerd).
