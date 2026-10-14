"""
Task 3 — Synthetic Offcut Matcher Prototype
-------------------------------------------
Purpose:
  Demonstrate how a read-only tool could shortlist steel offcuts for parts.

Important:
  - All records below are synthetic and illustrative.
  - This is a screening prototype, not production nesting software.
  - It does not validate steel certificates, heat numbers, cutting geometry,
    grain/orientation constraints, CNC constraints, or accounting policy.
  - It never automatically reserves/transfers material or claims savings.
"""

from dataclasses import dataclass, asdict
from typing import Optional
import csv

@dataclass
class Offcut:
    offcut_id: str
    project_id: str
    grade: str
    thickness_mm: float
    length_mm: float
    width_mm: float
    location: str
    certified: bool
    available: bool
    book_value_inr: float

@dataclass
class Part:
    part_id: str
    project_id: str
    grade: str
    thickness_mm: float
    length_mm: float
    width_mm: float
    new_material_cost_inr: float
    cross_project_policy: str  # "ALLOWED", "APPROVAL_REQUIRED", "PROHIBITED"

# Synthetic examples only — not client data.
OFFCUTS = [
    Offcut("O-101", "P-A", "S275", 10, 800, 600, "Rack-03", True, True, 6000),
    Offcut("O-102", "P-A", "S355", 10, 900, 500, "Rack-07", True, True, 7200),
    Offcut("O-103", "P-C", "S275", 12, 1000, 700, "Yard-02", True, True, 9000),
    Offcut("O-104", "P-B", "S275", 10, 700, 500, "Rack-01", False, True, 3500),
    Offcut("O-105", "P-D", "S275", 10, 900, 700, "Rack-09", True, False, 8000),
]

PARTS = [
    Part("PART-01", "P-B", "S275", 10, 500, 400, 8000, "ALLOWED"),
    Part("PART-02", "P-E", "S355", 10, 600, 400, 9500, "APPROVAL_REQUIRED"),
    Part("PART-03", "P-E", "S275", 10, 750, 550, 7000, "PROHIBITED"),
    Part("PART-04", "P-F", "S275", 12, 800, 600, 8500, "ALLOWED"),
]

# Illustrative incremental costs. Replace with measured client costs in a real pilot.
HANDLING_AND_INSPECTION_INR = 500
CUTTING_COST_INR = 700
TRANSFER_ADMIN_COST_INR = 250


def fits_rectangle(offcut: Offcut, part: Part) -> bool:
    """Simple rectangular fit check, allowing 90-degree rotation.
    Real nesting needs shape geometry, kerf, edge margins and CNC constraints.
    """
    direct = offcut.length_mm >= part.length_mm and offcut.width_mm >= part.width_mm
    rotated = offcut.length_mm >= part.width_mm and offcut.width_mm >= part.length_mm
    return direct or rotated


def evaluate(offcut: Offcut, part: Part) -> dict:
    reasons = []

    if not offcut.available:
        return result(offcut, part, "REJECTED", ["Offcut is not currently available."])

    if not offcut.certified:
        return result(offcut, part, "REJECTED", ["Certification/traceability is not confirmed."])

    if offcut.grade != part.grade:
        return result(offcut, part, "REJECTED", [f"Grade mismatch: {offcut.grade} vs {part.grade}."])

    if offcut.thickness_mm != part.thickness_mm:
        return result(offcut, part, "REJECTED", [f"Thickness mismatch: {offcut.thickness_mm} mm vs {part.thickness_mm} mm."])

    if not fits_rectangle(offcut, part):
        return result(offcut, part, "REJECTED", ["Offcut dimensions are insufficient for this simplified fit check."])

    same_project = offcut.project_id == part.project_id
    if not same_project and part.cross_project_policy == "PROHIBITED":
        return result(offcut, part, "REJECTED", ["Cross-project reuse is prohibited by the supplied policy."])

    incremental_cost = HANDLING_AND_INSPECTION_INR + CUTTING_COST_INR
    if not same_project:
        incremental_cost += TRANSFER_ADMIN_COST_INR

    # Conservative illustrative screen: don't assume book value is zero.
    total_reuse_cost = offcut.book_value_inr + incremental_cost
    net_advantage = part.new_material_cost_inr - total_reuse_cost

    if not same_project and part.cross_project_policy == "APPROVAL_REQUIRED":
        status = "REQUIRES_APPROVAL"
        reasons.append("Cross-project transfer requires Finance/project approval before any use.")
    elif net_advantage > 0:
        status = "ELIGIBLE"
        reasons.append("Engineering screen passed and illustrative reuse cost is below new-material cost.")
    else:
        status = "NOT_ECONOMIC"
        reasons.append("Illustrative reuse cost is not below new-material cost.")

    reasons.append("Candidate only: confirm physical identity, dimensions, certification, location, CNC feasibility and cost policy.")
    return {
        "part_id": part.part_id,
        "offcut_id": offcut.offcut_id,
        "offcut_project": offcut.project_id,
        "part_project": part.project_id,
        "status": status,
        "same_project": same_project,
        "offcut_book_value_inr": offcut.book_value_inr,
        "incremental_cost_inr": incremental_cost,
        "estimated_total_reuse_cost_inr": total_reuse_cost,
        "new_material_cost_inr": part.new_material_cost_inr,
        "illustrative_advantage_inr": net_advantage,
        "reasons": " ".join(reasons),
    }


def result(offcut: Offcut, part: Part, status: str, reasons: list[str]) -> dict:
    return {
        "part_id": part.part_id,
        "offcut_id": offcut.offcut_id,
        "offcut_project": offcut.project_id,
        "part_project": part.project_id,
        "status": status,
        "same_project": offcut.project_id == part.project_id,
        "offcut_book_value_inr": offcut.book_value_inr,
        "incremental_cost_inr": None,
        "estimated_total_reuse_cost_inr": None,
        "new_material_cost_inr": part.new_material_cost_inr,
        "illustrative_advantage_inr": None,
        "reasons": " ".join(reasons),
    }


def main():
    rows = []
    for part in PARTS:
        for offcut in OFFCUTS:
            rows.append(evaluate(offcut, part))

    # Keep only candidates that pass the basic engineering/data checks,
    # including candidates that require policy approval.
    shortlisted = [
        row for row in rows
        if row["status"] in {"ELIGIBLE", "REQUIRES_APPROVAL", "NOT_ECONOMIC"}
    ]
    shortlisted.sort(
        key=lambda r: (
            r["part_id"],
            {"ELIGIBLE": 0, "REQUIRES_APPROVAL": 1, "NOT_ECONOMIC": 2}.get(r["status"], 3),
            -(r["illustrative_advantage_inr"] or 0),
        )
    )

    output_path = "synthetic_offcut_matches.csv"
    if shortlisted:
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(shortlisted[0].keys()))
            writer.writeheader()
            writer.writerows(shortlisted)

    print("SYNTHETIC OFFCUT MATCHER — illustrative screening only")
    print("-" * 64)
    for row in shortlisted:
        advantage = row["illustrative_advantage_inr"]
        advantage_text = "n/a" if advantage is None else f"INR {advantage:,.0f}"
        print(
            f'{row["part_id"]:8} <- {row["offcut_id"]:6} | '
            f'{row["status"]:18} | illustrative advantage: {advantage_text}'
        )
        print(f'  Reason: {row["reasons"]}')
    print(f"\nWrote {len(shortlisted)} shortlisted rows to {output_path}")
    print("No material is reserved, transferred, or automatically approved.")


if __name__ == "__main__":
    main()
