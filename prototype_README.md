# Task 3 optional prototype — Synthetic offcut matcher

## What it demonstrates

This small Python prototype screens synthetic steel offcuts against synthetic parts. It checks:
- grade and thickness compatibility;
- simplified rectangular dimensions, allowing rotation;
- availability and a certification/traceability flag;
- whether cross-project use is allowed, requires approval, or is prohibited;
- an illustrative cost comparison using book value plus incremental handling, cutting and transfer costs.

It outputs candidate rows to `synthetic_offcut_matches.csv`.

## Run it

Requires Python 3.9+ and no third-party packages:

```bash
python synthetic_offcut_matcher.py
```

## Important limitations

- Every record and cost is synthetic and illustrative; no client data is included.
- Rectangle fit is only a coarse filter. Real nesting needs actual part geometry, kerf, edge margins, machine constraints and production rules.
- A boolean certification flag is not a substitute for verifying grade certificates, heat numbers and traceability.
- Costs and the accounting treatment of offcuts must be confirmed with the client.
- The prototype does not reserve material, write to Strumis/PLM, transfer costs, or authorize production.
- The correct output is a candidate shortlist for human review, not an automated decision or a claim of realized savings.
