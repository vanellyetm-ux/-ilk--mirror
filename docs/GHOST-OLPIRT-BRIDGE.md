# GHOST–OLPIRT Bridge: $ilk mirror, Ash, and external AshShow/V

## Purpose
Connect the $ilk mirror's Vœ provenance and recovery model to the writable Ash knowledge destination while retaining AshShow/V as an optional external presentation target. This is a controlled, inspectable integration—not a hidden transfer mechanism.

## Confirmed repository facts
- Source: `vanellyetm-ux/-ilk--mirror`, default branch `main`.
- Ash: `vanellyetm-ux/Ash`, default branch `main`; repository identity and write permission confirmed.
- Lumi: `vanellyetm-ux/Lumi`; narrative entry point proposed through its own feature branch and PR.
- AshShow/V: a distinct user-designated organization destination. The exact target repository and organization-side acceptance remain unresolved. It is not aliased to Ash and is not required for the Ash or Lumi PRs.
- VaN Knowledge HQ: curated in this source repository, with structured knowledge proposed in Ash and a narrative landing page proposed in Lumi.

## Narrative design
The bridge turns narrative into a traceable knowledge journey:
1. **Origin / OLPIRT** — preserve authored narrative, context, source commit, and path.
2. **BOF / Foundation** — distinguish observation, interpretation, proposal, and unresolved question.
3. **GHOST / Translation** — normalize narrative into structured records without erasing uncertainty or lineage.
4. **$ilk Mirror / Reflection** — preserve source references, immutable history, and content digests.
5. **Ash / Knowledge foundation** — curate structured records, reusable context, and topic indexes.
6. **VaN Knowledge HQ / Stewardship** — curate, review, cross-link, and promote records under human approval.
7. **AshShow/V / Optional presentation** — a separately authorized downstream surface, only if and when an organization maintainer accepts a handoff.

Ash and AshShow/V remain separate destinations. A successful Ash PR does not imply AshShow acceptance or authorization.

## Transfer lifecycle
`DISCOVER → PROPOSE → AUTHORIZE → STAGE → VERIFY → ACCEPT`

Failures move to `PENDING_REVIEW` or `REJECTED`; they never imply success.

## Required controls
- Human approval scoped to destination repository, branch, paths, and operation.
- Feature branches only; no direct default-branch writes or force pushes.
- Exclude secrets, tokens, private keys, and secret-bearing environment values.
- Record source repository, ref, commit, path, SHA-256, and narrative classification.
- Verify destination readback against expected digest and commit identity.
- Maintain separate receipts for each destination that actually receives a transfer.
- Synthetic/demo evidence remains explicitly labelled and cannot be promoted as live evidence.

## Transfer envelope
See `integrations/ghost-olpirt/transfer.schema.json`. Every actual destination transfer uses a separate envelope and independent verification state.

## Current implementation state
- Vœ anchor/recovery implementation: source code inspected in the mirror.
- GHOST local foundation: archive-inspected; local unit tests were reported passing in the supplied archive workspace. No live remote-write capability is claimed.
- Ash: repository identity and write permission verified; knowledge implementation proposed in [Ash PR #1](https://github.com/vanellyetm-ux/Ash/pull/1).
- Lumi: narrative entry point proposed in [Lumi PR #3](https://github.com/vanellyetm-ux/Lumi/pull/3).
- AshShow/V: external presentation handoff documented only; no AshShow write is attempted or required for these PRs.
- Live end-to-end transport: not configured or verified.
- Default branches: unchanged by this integration work.
