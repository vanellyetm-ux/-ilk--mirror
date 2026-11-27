# GHOST–OLPIRT multi-destination adapter

This integration uses independently reviewable repositories and does not require write access to the AshShow organization.

## Writable implementation destinations

- **Ash** — confirmed repository `vanellyetm-ux/Ash`; implementation is proposed in [Ash PR #1](https://github.com/vanellyetm-ux/Ash/pull/1).
- **Lumi** — confirmed repository `vanellyetm-ux/Lumi`; narrative entry point is proposed in [Lumi PR #3](https://github.com/vanellyetm-ux/Lumi/pull/3).

## External presentation destination

- **AshShow/V** — retained as a downstream presentation target. This PR documents the handoff boundary only; it does not create or modify an AshShow repository, branch, file, or PR. Exact target repository identity and organization-side acceptance remain external follow-up work.

Each writable repository has its own feature branch, review, readback verification, and receipt. Acceptance by Ash or Lumi does not imply acceptance by AshShow/V, or vice versa.

The narrative contract preserves authored text and origin while classifying each statement as observation, interpretation, proposal, or question. See `../../docs/GHOST-OLPIRT-BRIDGE.md` and `../../docs/VAN-KNOWLEDGE-HQ.md`.

Do not store secrets in manifests or source. Do not write default branches, use hidden transfers, or bypass review.
