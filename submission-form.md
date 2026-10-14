# Task 3 — Forward Deployed Engineer Case Study
## Submission Form — Client B: Structural Steel

**Candidate:** Krushna Raut  
**Case study:** `case_study.pdf` (LaTeX source: `case_study.tex`)  
**Client note:** `client-note.pdf` (LaTeX source: `client-note.tex`)  
**Confidentiality:** Client discovery notes are confidential and are not included in any public repository.

---

## 1. The real problem vs. the client's ask

**Client's ask:** Explore how AI can improve nesting and reduce steel waste, with nesting as the first area to investigate.

**Real problem:** The client lacks a reconciled, trustworthy baseline for material loss and preventability, has not verified whether Strumis automatic nesting performs worse than manual planning, and cannot yet quantify the value or business feasibility of offcut reuse and drawing-revision losses.

## 2. Stakeholders and what they need

- **Cost Control / sponsor:** a defensible baseline, an understandable business case, and a short management update.
- **Nesting lead and planners:** feasible cutting plans, preservation of shop-floor rules, and a fair comparison that does not presume manual or automatic nesting is superior.
- **Finance / project accounting:** project-level cost integrity, traceable inventory movements, and explicit approval/valuation rules before cross-project transfers.
- **Engineering / drawing office:** current drawing revisions, part-level traceability, and separation of client-caused changes from internal errors.
- **Yard / stores:** reliable offcut identity, dimensions, grade, location, and retrieval status.
- **Planning / procurement / factory operations:** material availability, delivery-date protection, and no disruption to CNC throughput.
- **Management:** a low-risk, stage-gated recommendation and evidence of value before funding implementation.
- **IT / system owners:** read-only access, clear source-of-truth mapping between Strumis and PLM, data security, and no unapproved write-back.

## 3. Five ranked questions for the next call

1. **Can we obtain a read-only sample of nesting, part, purchase, scrap and offcut records, and which system is authoritative for each field (Strumis or PLM)?**  
   **Why:** This is the data-readiness gate for a defensible baseline and fair comparison.  
   **Assumption pending answer:** Some data can be exported or manually sampled; historical records may be split across systems during migration.

2. **How does the nesting team decide that manual nesting is better than Strumis automatic nesting, and what constraints/settings are used?**  
   **Why:** The reported difference may reflect configuration or unwritten shop-floor rules rather than an inherent limitation of the software.  
   **Assumption pending answer:** The existing automatic feature has not yet been tested under a jointly agreed, representative configuration.

3. **How are the reported plate, profile and overall waste percentages calculated, and what counts as usable offcut, scrap, kerf and revision loss?**  
   **Why:** The reported ranges may use different denominators and may not reconcile.  
   **Assumption pending answer:** Definitions differ or some loss categories are not consistently recorded; we will not treat the current percentages as a validated baseline.

4. **Can an offcut move between projects, who approves it, and how is its value credited/debited? Is the restriction contractual or internal policy?**  
   **Why:** Geometric fit does not establish engineering suitability, availability, or permission to transfer the cost.  
   **Assumption pending answer:** Cross-project reuse requires Finance approval; no transfer or savings is assumed until policy is confirmed.

5. **How are drawing revisions recorded, and can client-caused revisions be linked to material already cut and claims submitted?**  
   **Why:** Potentially claimable revision losses may be a nearer-term recovery opportunity than a new optimizer, but it must be evidenced.  
   **Assumption pending answer:** Revision history is incomplete or fragmented; no recoverable amount is assumed before reviewing records and contract terms.

## 4. Options considered and recommendation

- **Reporting/baseline only:** required foundation, but insufficient alone to test the manual-versus-auto claim.
- **Configure and compare Strumis auto-nesting against manual plans:** included in the core pilot; tests the central claim before buying or building.
- **Read-only offcut registry audit and matcher:** limited, conditional proof of concept; returns candidate matches only.
- **Custom AI/deep-learning nesting optimizer:** deferred because the existing capability has not been fairly tested and the required data/rules are not yet established.
- **Buy a commercial nesting package:** deferred until the bake-off establishes a concrete gap and a requirements baseline.
- **Automatic cross-project allocation:** excluded until Finance establishes ownership, approval and cost-transfer rules.
- **Yard digital twin / new trailer system:** not part of this pilot. Yard conditions may change when held projects restart; CarTrack and booking tools already exist and should first be analysed.
- **Drawing-revision tracking:** early follow-on candidate because client-caused revisions may be claimable, subject to evidence and contract rules.

**Recommendation:** a six-week, stage-gated “Measure and Prove” pilot: data readiness and baseline first; a controlled manual-versus-Strumis comparison second; offcut matching only in read-only/shadow mode if data quality permits. No custom optimizer or production write-back during the pilot.

## 5. Evaluation plan

- **Primary measures:** purchased-material mass balance and finished-part yield, calculated from agreed, reconciled weights. Report separately: finished-part material, process loss (including kerf/trim where measurable), usable offcut inventory, scrap/recovered scrap, revision-related loss, and unexplained difference. Do not count stored offcuts as realized savings.
- **Secondary measures:** feasibility pass rate against agreed engineering/CNC constraints; planner time per job; offcut candidates accepted by the nesting lead; tonnes of fresh steel actually avoided where traceable.
- **Baseline:** target up to 60 representative plates/jobs, stratified by grade/thickness and job type, subject to availability and data quality. The baseline is preliminary if weights cannot be reconciled.
- **Nesting comparison:** target up to 40 comparable historical jobs with the same part list and constraints; compare existing manual plans with Strumis auto plans. Blind A/B review where practical. Report paired differences and uncertainty based on observed variability; this pilot sample is not guaranteed to provide statistical power.
- **Proposed decision rules (agree with client before examining results):** consider adopting configured auto-nesting as a first draft only if feasibility requirements are met and yield is practically non-inferior to manual while planner time improves meaningfully. A one-percentage-point yield tolerance and 30% planner-time reduction may be discussed as provisional targets, not validated facts. If results are inconclusive, do not claim superiority; extend testing or retain current process.
- **Offcut matcher:** historical replay in read-only mode; report candidate count, engineering acceptance, data completeness, and potential fresh-steel avoidance. Cross-project matches remain flagged for Finance approval. Acceptance percentage is descriptive until a representative sample is available.
- **Who measures:** delivery analyst calculates; nesting lead judges feasibility; Cost Control approves financial definitions; Finance approves transfer rules; IT validates data sources.
- **Stop / redirect:** stop or re-scope if essential data cannot be obtained/reconciled by the end of week 2; if plans cannot be judged consistently; or if no addressable opportunity is evidenced relative to the client's agreed hurdle rate. If cross-project transfer is disallowed, exclude it from the value case and continue only if same-project reuse or the nesting comparison independently justifies the work.

## 6. Cost, price and value

**Indicative delivery-cost estimate for six weeks (assumptions, not company-validated rates):**

- FDE: ₹3.0 lakh/month × 1.0 FTE × 1.5 months = ₹4.50 lakh.
- Data/analytics engineer: ₹2.4 lakh/month × 1.0 FTE × 1.5 months = ₹3.60 lakh.
- Project lead/QA: ₹3.0 lakh/month × 0.25 FTE × 1.5 months = ₹1.125 lakh (rounded to ₹1.13 lakh).
- Travel/site visits: ₹1.00 lakh allowance.
- Tools/hosting: ₹0.30 lakh allowance.
- **Estimated delivery cost: ₹10.53 lakh.**

**Illustrative proposed client fee:** ₹18.00 lakh fixed fee, subject to confirming scope, staffing, travel, data access and tax. Difference from estimated delivery cost is ₹7.47 lakh (about 41.5% of the fee) before tax, overhead and unmodelled risks; this is not a validated margin or contingency calculation. Proposed milestones: 30% kickoff (₹5.4 lakh), 40% baseline (₹7.2 lakh), 30% final readout (₹5.4 lakh). Ongoing hosting/support cost is not confirmed and must be scoped before production use. Estimated client contribution: approximately 50–55 staff-hours over six weeks.

**Illustrative value sensitivity, not a forecast:** if verified throughput is 80,000 tonnes/year and an attributable improvement prevents 0.5 percentage points of purchased steel from becoming unrecovered loss, that equals 400 tonnes. At an assumed net avoidable cost of ₹30,000/tonne (illustrative steel cost ₹60,000/t less ₹30,000/t scrap recovery), the theoretical annual value is ₹1.2 crore. This is not a savings promise: throughput, purchase and scrap prices, material mix, loss definition, attainable improvement, and whether the reduction actually avoids purchases must all be verified. Stored offcuts do not count as savings until used to avoid a purchase or cost. Revision-claim recovery and trailer-hire reductions are unquantified.

## 7. Timeline and dependencies

- **Week 0:** kickoff, confidentiality agreement, named owners, data-access request.
- **Weeks 1–2:** map Strumis/PLM sources, validate exports and IDs, agree definitions, shadow nesting, inspect available trailer data. **Go/no-go gate at end of week 2.**
- **Week 3:** preliminary baseline and data-quality report.
- **Weeks 3–5:** manual-versus-auto comparison and feasibility review, subject to representative records.
- **Weeks 4–6:** offcut-matching historical replay in read-only mode, only if the register is sufficiently complete.
- **Week 6:** findings, uncertainty/limitations, and recommendation: tune, track, buy, build, investigate revision claims, redirect to trailers, or stop.

**Dependencies:** read-only access; system-owner support; representative jobs; nesting-lead availability; Finance's transfer/cost policy; engineering interpretation of revisions; purchase/scrap records where available.

## 8. Where I would push back or narrow the ask

- Did not accept “AI for nesting” as proof that a new AI model is needed; proposed testing the existing Strumis automatic feature first.
- Did not treat 7–10% overall and 20–25% plate wastage as a verified baseline; asked for definitions and reconciliation.
- Did not accept “manual is better” as established fact because it was relayed second-hand; proposed a controlled comparison.
- Did not recommend automatic cross-project material allocation without engineering compatibility, availability, Finance approval and cost-transfer rules.
- Did not promise savings from stored offcuts; only avoided purchases/costs supported by evidence can count.
- Kept yard digital-twin work and fleet optimisation outside the core pilot; the yard situation may change when held projects restart, and existing equipment data tools have not been fully analysed.
- Made the custom optimizer a later option only if the evidence shows a material gap that existing software cannot close.

## 9. What could go wrong / what information I do not fully trust

- Historical data may be split between Strumis and PLM during migration; do not assume Strumis contains all 12 months of records.
- “Manual beats auto” is a second-hand claim, not a measured result.
- Waste percentages may use different denominators or treatment of offcuts and scrap; they do not yet reconcile to a common mass balance.
- Offcuts said to be recorded and checked may still have missing dimensions, grade, certification, location or status.
- The contact is from Cost Control and said they do not know nesting in detail; nesting, engineering and yard assumptions must be validated directly.
- Project-level cost allocation may be contractual or an internal convention; Finance must clarify.
- Current projects are on hold and may not represent normal operating conditions.
- The 80,000 t/year figure conflicts with a reported 7,000–8,000 t/month run rate (84,000–96,000 t/year); actual throughput must be confirmed.
- All delivery rates, steel prices, scrap recovery values, target thresholds and the proposed fee are assumptions until validated.

## 10. AI usage

**Tools used:** ChatGPT (OpenAI).  
**Helped with:** structuring the case study and client note; reviewing the discovery notes; identifying missing questions, stakeholder constraints, metric/financial assumptions, and risks; drafting and revising LaTeX and Markdown; checking arithmetic and improving clarity.  
**Misled / needed correction:** Early drafts treated some assumed values and thresholds too confidently, described a potential waste split before the data was validated, and had LaTeX table-width/layout problems. These were revised by labelling assumptions, separating loss categories, qualifying the evaluation protocol and value sensitivity, and checking the compiled output. This answer reflects the actual assistance used in preparing these materials; edit it if any detail is inaccurate.  
**Discarded:** Building a custom AI/deep-learning nesting engine before testing Strumis; automatic cross-project allocation before Finance approval; treating the client's waste estimates as verified; presenting the illustrative value calculation as guaranteed savings.

## 11. GitHub repository

**Repository URL:** https://github.com/kru5hna/Case-Study

**Submission checklist**
- [x] Compile `case_study.tex` to `case_study.pdf`; verify no more than six main pages plus appendix.
- [x] Compile `client-note.tex` to exactly one page.
- [x] Insert actual GitHub repository URL after creating the repository.
- [x] Confirm all assumptions and AI-usage disclosure are accurate.
- [x] Ensure no confidential discovery notes are in the repository.
