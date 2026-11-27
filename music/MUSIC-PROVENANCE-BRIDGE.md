# Music Provenance Bridge

The $ilk Mirror is the lineage and review bridge for the VaN music creation stream.

## Connected destinations

- Private production library: [Vanellye/DataEnvelopeMint](https://github.com/Vanellye/DataEnvelopeMint)
- Public narrative stream: [vanellyetm-ux/Lumi — Music Main Stream](https://github.com/vanellyetm-ux/Lumi/blob/main/MUSIC-MAIN-STREAM.md)
- Seed repositories: CodEXgen, CodEXgen-2, Ash, Y-, WANA, Manticore, write-access, and this mirror

## Responsibilities

1. Preserve the source repository and path for every musical seed.
2. Keep source sketches distinct from new lyrics, arrangements, and generated audio.
3. Record transformations: motif changes, tempo/meter changes, orchestration, lyric revisions, and render settings.
4. Maintain checksums and render receipts for produced files.
5. Track visibility and rights before any asset is linked into a public stream.
6. Keep human review and release authorization explicit.

## Envelope fields

Each music asset should carry:

- `asset_id`, `track_id`, and `asset_type`
- `source_refs[]` with repository, path, and revision
- `transformation_notes`
- `rights_status` and `visibility`
- `toolchain`, `render_settings`, and `output_hash`
- `validation_status`, `reviewer`, and `approval_receipt`

## Promotion flow

`SOURCE_CAPTURED → LINEAGE_RECORDED → COMPOSITION_REVIEWED → RENDER_VERIFIED → HUMAN_APPROVED → LUMI_STREAM`

The mirror does not silently copy private source material into public repositories. It records references and evidence while preserving the source repository's access boundary.

## Canonical stream

[Open the DataEnvelopeMint Music Main Stream Frame](https://github.com/Vanellye/DataEnvelopeMint/blob/main/music/MAIN-STREAM.md)
