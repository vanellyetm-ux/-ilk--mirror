# GHOST–OLPIRT Bridge: $ilk mirror, AshShow/V, and Ash

## Purpose
Connect the $ilk mirror's Vœ provenance and recovery model to two peer destinations: **AshShow/V** and **Ash**. This is a controlled, inspectable integration—not a hidden transfer mechanism.

## Confirmed repository facts
- Source: `vanellyetm-ux/-ilk--mirror`, default branch `main`.
- Ash: `vanellyetm-ux/Ash`, default branch `main`; repository identity and write permission confirmed.
- AshShow/V: a distinct user-designated destination. Exact GitHub owner/repository identity remains pending. Do not alias it to Ash.
- VaN Knowledge HQ: curated in this source repository and mirrored as a knowledge landing page in Lumi.

## Narrative design
The bridge turns narrative into a traceable knowledge journey:
1. **Origin / OLPIRT** — preserve authored narrative, context, source commit, and path.
2. **BOF / Foundation** — distinguish observation, interpretation, proposal, and unresolved question.
3. **GHOST / Translation** — normalize narrative into structured records without erasing uncertainty or lineage.
4. **$ilk Mirror / Reflection** — preserve source references, immutable history, and content digests.
5. **AshShow/V / Presentation** — narrative-facing knowledge and context surface.
6. **Ash / Knowledge foundation** — structured records, reusable context, and topic indexes.
7. **VaN Knowledge HQ / Stewardship** — curate, review, cross-link, and promote records under human approval.

Ash and AshShow/V are independent peers. Each destination requires its own transfer manifest, authorization, branch, verification, and receipt.

## Transfer lifecycle
`DISCOVER → PROPOSE → AUTHORIZE → STAGE → VERIFY → ACCEPT`

Failures move to `PENDING_REVIEW` or `REJECTED`; they never imply success.

## Required controls
- Human approval scoped to destination repository, branch, paths, and operation.
- Feature branches only; no direct default-branch writes or force pushes.
- Exclude secrets, tokens, private keys, and secret-bearing environment values.
- Record source repository, ref, commit, path, SHA-256, and narrative classification.
- Verify destination readback against expected digest and commit identity.
- Maintain separate Ash and AshShow/V transfer receipts.
- Synthetic/demo evidence remains explicitly labelled and cannot be promoted as live evidence.

## Transfer envelope
See `integrations/ghost-olpirt/transfer.schema.json`. Every destination uses a separate envelope and independent verification state.

## Current implementation state
- Vœ anchor/recovery implementation: source code inspected in the mirror.
- GHOST local foundation: archive-inspected; local unit tests reported passing.
- Ash repository: identity and write permission verified; separate destination branch scaffold exists.
- AshShow/V repository: identity and permissions pending; no destination writes.
- Live end-to-end transport: not configured or verified.
- Default branches: unchanged by this scaffold.
