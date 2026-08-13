"""Write the consolidated finite-contract gate from existing evidence."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTRACTS = ("C1", "C2", "C3", "C4", "C5", "C6")


def main() -> None:
    verification = json.loads((ROOT / "outputs" / "verification.json").read_text())
    statuses = {
        claim: "FINITE_CONTRACT_PASS"
        if verification["claims"][claim]["status"] == "verified"
        else "FINITE_CONTRACT_FAIL"
        for claim in CONTRACTS
    }
    passed = sum(status == "FINITE_CONTRACT_PASS" for status in statuses.values())
    gate = {
        "paper": verification["paper"],
        "gate": "finite-contract-audit",
        "tests_passed": passed == len(CONTRACTS),
        "publication_gate_passed": passed == len(CONTRACTS),
        "finite_contracts_passed": passed,
        "finite_contracts_total": len(CONTRACTS),
        "paper_claims_verified": 0,
        "paper_claims_total": len(CONTRACTS),
        "overall_status": "INCONCLUSIVE",
        "contract_statuses": statuses,
        "source_sha256": verification["source_sha256"],
        "scope": (
            "Six source-pinned finite source/formula/control contracts pass; "
            "PPAD/PLS reductions, universal tractability, and complexity lower "
            "bounds remain independently unverified."
        ),
    }
    encoded = json.dumps(gate, indent=2) + "\n"
    (ROOT / "outputs" / "publication_gate.json").write_text(encoded)
    (ROOT / "publication_gate.json").write_text(encoded)
    print(json.dumps(gate, indent=2))


if __name__ == "__main__":
    main()

