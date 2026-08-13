# Publication gate

This repository is gate-ready as a finite source/formula/control audit.

- Finite contracts: 6/6 pass.
- Paper-level claims independently verified: 0/6.
- Overall status: **INCONCLUSIVE**.
- Gate output: [publication_gate.json](publication_gate.json).
- Raw output: [outputs/verification.json](outputs/verification.json).

Run:

```bash
uv sync --frozen
uv run python repro/src/run_publication_gate.py
```

The gate checks source anchors, selected finite controls, and negative controls.
It does not establish PPAD/PLS hardness, universal reductions, or asymptotic
complexity results.
