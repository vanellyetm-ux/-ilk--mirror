# VaN Knowledge HQ

## Narrative
VaN Knowledge HQ is the stewardship layer connecting origin, meaning, evidence, implementation, and accountable promotion. Knowledge is not merely copied between repositories: it retains its authored context, provenance, confidence, and review history.

## Knowledge journey
| Stage | Role | Output |
|---|---|---|
| Origin / OLPIRT | Preserve the narrative and its source | Source-linked narrative record |
| BOF / Foundation | Separate observation, interpretation, proposal, and question | Classified evidence record |
| GHOST | Translate narrative into structured knowledge | Normalized knowledge object |
| $ilk Mirror | Reflect and preserve source lineage | Immutable source reference and digest |
| AshShow/V | Present narrative and its meaning | Narrative-facing knowledge view |
| Ash | Hold structured, reusable knowledge | Topic index and linked records |
| VaN HQ | Govern curation and promotion | Reviewed, traceable knowledge catalogue |

## Promotion levels
- `DRAFT`: newly captured; not yet reviewed.
- `SOURCE_VERIFIED`: source path/ref/commit inspected.
- `EVIDENCE_REVIEWED`: claims checked against cited evidence; uncertainty retained.
- `IMPLEMENTATION_VERIFIED`: tests or reproducible execution validate implementation claims.
- `PROMOTION_APPROVED`: a human reviewer explicitly approves publication to a named destination.
- `PUBLISHED`: destination readback and receipt verified.

Levels do not advance automatically. A submitted write is not a publication receipt.

## Starter knowledge domains
1. $ilk / Vœ provenance and recovery.
2. GHOST local gateway, adapter boundaries, and explicit capability limits.
3. OLPIRT narrative and source continuity.
4. BOF narrative classification, maturation, and mitigation.
5. AshShow/V presentation model.
6. Ash structured knowledge foundation.
7. Git Freedom Bridge and reviewable repository mutations.
8. PONS / human authorization and evidence governance.
9. VaN principles: preserve provenance, surface uncertainty, and keep automation accountable to people.

## Evidence labels
- `SOURCE_VERIFIED`: inspected in a named repository/ref/path.
- `ARCHIVE_VERIFIED`: inspected in a user-supplied archive.
- `TEST_VERIFIED`: reproducible command completed; include output and scope.
- `CONFIGURED_NOT_EXECUTED`: configuration exists but live execution has not occurred.
- `PROPOSED`: design only.
- `UNVERIFIED`: no supporting evidence.

## Seed evidence
### Vœ mirror
The source repository contains `anchor/voe/live_api.py`, `anchor/voe/recovery.py`, write-access fixtures, transient anchors, and a manually dispatched workflow. The recovery evaluator requires authorization, a valid commit SHA, matching readback commit, and byte-identical readback before accepting a write.
Class: `SOURCE_VERIFIED` (code inspection only; not a production test).

### GHOST backend archive
The supplied `CodEXgen-GHOST-OLPIRT.zip` contains a local CLI foundation. Its documentation says GitHub write capability is not implemented, and its provenance manifest flags live OpenAI, live CodeQL, and remote writes as false.
Class: `ARCHIVE_VERIFIED`.

### Local tests
Command reported: `python -m unittest ghost_backend.test_gateway -v`.
Result reported: seven tests passed in the extracted archive workspace on 2026-11-27. This is a local test result, not proof of live service connectivity.
Class: `TEST_VERIFIED`.

### Ash destination
`vanellyetm-ux/Ash` is a separate repository. A feature branch named `integration/ghost-olpirt-knowledge-hq` was created; default branch has not been changed by this work.
Class: `SOURCE_VERIFIED`.

### AshShow/V destination
A separate peer destination requested by the user. Exact GitHub repository identity and permissions remain unresolved. It must not be treated as an alias for Ash.
Class: `PROPOSED`.

## Promotion rules
Every record needs a stable source locator, commit or archive digest, evidence class, validation method, and reviewer reference where operational claims are involved. Publication to each destination requires a separate approved scope, feature branch, destination readback, and receipt.

## Change log
- 2026-11-27: Initial VaN HQ catalogue and narrative pipeline designed for both AshShow/V and Ash.
