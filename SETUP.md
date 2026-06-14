# Setup: using this wiki with Obsidian

This wiki is a plain folder of markdown files, which is exactly what an Obsidian vault is. Obsidian is the reader and IDE, the LLM (Claude) is the writer, and this folder is the vault. You browse and direct in Obsidian while Claude does the writing and bookkeeping in the same files. Edits appear live because Obsidian watches the filesystem.

## One-time setup

1. Install Obsidian from https://obsidian.md (free).
2. Open this folder as a vault. In Obsidian, choose "Open folder as vault" and select the `GenAI-Wiki` folder (the one containing `CLAUDE.md`, `index.md`, `log.md`, and `wiki/`). Open the root, not a subfolder, so the `[[wikilinks]]` resolve across `wiki/`, `wiki/sources/`, and so on. Obsidian matches `[[slug]]` by filename across the whole vault.
3. Start at `index.md` and navigate by clicking the `[[links]]`.

## Recommended settings and plugins

- Graph view (left ribbon, or Cmd/Ctrl-G) shows the whole structure: hubs, clusters, and orphans. Local graph shows just the current note's neighborhood.
- The backlinks and outgoing-links panes (right sidebar) show what references the current page and where to add cross-links.
- Dataview (Settings, Community plugins, Browse, install and enable "Dataview") powers [[dashboard]], which builds tables from page frontmatter. Until it is enabled, `dashboard.md` shows the raw query code.
- The Web Clipper browser extension converts an article to markdown straight into `raw/`, which is the fastest way to add a source.
- Marp (optional community plugin) renders a wiki page as a slide deck from its markdown.

## The daily loop

- To browse: open Obsidian, start at `index.md`, follow links, and use Graph view for the shape.
- To grow it: drop a source into `raw/` (or paste a link or idea to Claude) and say "ingest this." Claude reads it, updates the relevant pages, and appends to `log.md`. No refresh is needed.
- To clean up: ask Claude to "lint the wiki" from time to time, and it will find contradictions, stale claims, orphans, and missing cross-links.

## Conventions (maintained by Claude)

- Every page has YAML frontmatter (`title`, `type`, `created`, `updated`, `tags`, `sources`), which is what makes [[dashboard]] work. Keep the keys consistent if you edit by hand.
- Links are `[[slug]]` by filename. `index.md` is the catalog, `log.md` is the history, and `CLAUDE.md` is the schema Claude follows.

## Optional: version history with git

The vault is just text, so git gives you free history, diffs, and undo, which is handy since an ingest can touch many files:

```
cd GenAI-Wiki
git init && git add . && git commit -m "initial wiki"
```

See `.gitignore` for what is excluded. The Obsidian Git community plugin can auto-commit on a timer if you want hands-off backups.
