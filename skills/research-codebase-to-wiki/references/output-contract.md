# Offline Wiki Output Contract

## Directory

Every deliverable contains:

```text
wiki/
├── README.md
├── index.html
├── wiki.css
├── wiki.js
└── wiki-manifest.json
```

Additional local images or data files are allowed when necessary. Keep them inside the same directory and include their hashes in the manifest when they are load-bearing.

## Offline safety

- Do not load remote JavaScript, CSS, fonts, images, iframes, video, audio, or tracking pixels.
- External citations may be ordinary links and open only after an explicit user action.
- Escape repository text and code before insertion. Never inject source HTML as executable wiki markup.
- Do not use inline scripts, HTML event-handler attributes, CSS imports, or JavaScript networking.
- Do not require a build step, package manager, or server for basic reading.
- JavaScript enhances search, navigation, tabs, copying, theme, and local progress only; core content remains readable without it.
- Persist UI preferences only in `localStorage`; never store repository content or secrets there.

## Required usability

- semantic headings and landmarks;
- keyboard-accessible navigation and controls;
- visible focus states;
- desktop and narrow-screen layouts;
- light/dark theme using shared tokens;
- full-text section filtering;
- active-section navigation and reading progress;
- code blocks with wrapping or contained horizontal scrolling;
- diagrams that do not overflow the reading surface;
- reduced-motion behavior when animation is present.

Do not add a control unless it has real behavior.

## Section source anchors

Use repository-relative paths and optional symbols. Mark machine-checkable anchors with `data-source-path`:

```html
<code data-source-path="src/example.py">src/example.py::run</code>
```

The validator checks the file portion against `--source-root`. The visible text may include a symbol or explanation.

## Manifest

`wiki-manifest.json` records at least:

```json
{
  "schema_version": 1,
  "generated_by": "research-codebase-to-wiki",
  "skill_revision": "<commit or working-tree>",
  "profile": "product-architecture",
  "source_root_name": "example",
  "source_commit": "<commit or unversioned>",
  "source_dirty": false,
  "generated_at": "<RFC 3339 UTC>",
  "authority_files": ["README.md"],
  "evidence_status": {
    "implemented": 0,
    "partial": 0,
    "planned": 0,
    "declared": 0,
    "inferred": 0,
    "unknown": 0,
    "superseded": 0
  },
  "unverified_claims": [],
  "output_files": {
    "index.html": "sha256:..."
  }
}
```

The manifest is provenance, not a claim that the source repository is clean or the wiki exhaustive. Pass evidence counts and unresolved claims to the scaffold with repeatable `--evidence-count STATUS=COUNT` and `--unverified-claim TEXT` arguments so the README and manifest agree.

## README

State what snapshot and profile the wiki explains, how to open it, a recommended reading route, known evidence limits, and that UI state remains local to the browser.

## Validation

Run:

```bash
python3 scripts/validate_wiki.py WIKI_DIR --source-root REPOSITORY_ROOT
```

The validator checks structure, manifest fields and hashes, offline resource loading, internal anchors, local files, unresolved template markers, and declared source paths. Visual quality and factual correctness still require human inspection.
