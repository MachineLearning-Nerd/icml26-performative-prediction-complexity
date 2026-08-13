# On the Computational Complexity of Performative Prediction — finite audit report

Paper: Ioannis Anagnostides, Rohan Chauhan, Ioannis Panageas, Tuomas Sandholm,
and Jingming Yan, “On the Computational Complexity of Performative Prediction,”
[arXiv:2601.20180v1](https://arxiv.org/abs/2601.20180),
OpenReview [kkhVljGiMS](https://openreview.net/forum?id=kkhVljGiMS).

## Consolidated result

- Finite contracts: **6/6 pass**.
- Paper-level claims independently verified: **0/6**.
- Overall: **INCONCLUSIVE**.

The raw producer output uses `verified`; that label means the finite
contract passed. It does not mean that a PPAD/PLS reduction, universal
tractability result, query lower bound, or asymptotic complexity theorem has
been proved by this repository.

The pinned source archive is
`source/arxiv-2601.20180.tar`, SHA-256
`c32199596640624de68ae92f19d4db2324d837580da51db25910213388262b76`.

## What is actually run

The committed producer is
`repro/src/verify_performative_complexity.py`. It:

1. verifies the source archive hash;
2. extracts selected source files and checks theorem/corollary anchor tokens;
3. checks finite threshold, affine fixed-point, monotone scaling, and local
   objective examples;
4. executes two negative controls; and
5. writes `outputs/verification.json`.

The publication runner
`repro/src/run_publication_gate.py` invokes the producer and the
standard-library regression test. The notebook is explanatory and is not used
as the consolidated paper-level verifier.

## Claim-by-claim ledger

| Claim | Paper object | Finite producer check | Result and boundary |
| --- | --- | --- | --- |
| C1 | Theorem 3.4 PPAD-completeness threshold | Source anchors plus four `epsilon`/`rho` relationships using `epsilon'=0.088/6`; an incorrect denominator is rejected. | Finite contract pass; no affine-VI reduction or PPAD-hardness proof. |
| C2 | Quadratic/affine special case | Source anchor plus four affine fixed-point residual cells; a perturbed fixed point is rejected. | Finite contract pass; no complete quadratic/affine hardness reduction. |
| C3 | Theorem 3.5 tractability window | Source anchor plus four monotone `epsilon^4` scale values. | Finite contract pass; no ellipsoid proof or all-instance complexity bound. |
| C4 | Corollary 3.7 query lower bound | Source anchor plus 12 monotone `2^d` query-scale values. | Finite contract pass; no HPS hiding-game implementation or lower-bound proof. |
| C5 | Theorem 3.12 convex-domain hardness | Source anchor for a well-bounded convex domain. | Finite contract pass; no committed Sperner reduction or universal hardness proof. |
| C6 | Theorem 4.4 strategic-classification PLS-hardness | Source anchor plus one finite strict-local-objective check. | Finite contract pass; no committed local-max-cut reduction or PLS-hardness proof. |

## Negative controls

The producer requires these failure-seeking checks to remain active:

- a nearby incorrect denominator for `epsilon'` is rejected;
- a perturbed affine fixed point fails the residual check.

These controls increase confidence that the finite formulas are wired as intended.
They do not expand the checked domain to the paper’s universal statements.

## Reproduce

```bash
uv sync --frozen
uv run python repro/src/run_publication_gate.py
```

The lightweight consolidated summary is:

```bash
uv run python repro/src/finalize_gate.py
```

## Limitations

- Source-token presence is not a proof that every displayed derivation is correct.
- Finite cells cannot establish PPAD/PLS hardness, universal reductions,
  worst-case polynomial algorithms, exponential query lower bounds, or
  asymptotic rates.
- The notebook contains simplified demonstrations, including an
  ellipsoid-style example; those demonstrations are not paper-level proofs.
- The audit relies on the cited prior hardness results and does not re-prove
  those source problems.
- No empirical benchmark or author implementation is claimed here.

This report intentionally uses conservative language so the repository’s status
matches the code that actually runs.
