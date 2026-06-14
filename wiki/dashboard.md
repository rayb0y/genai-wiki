---
title: Dashboard
type: dashboard
created: 2026-06-08
updated: 2026-06-08
tags: [meta, dashboard]
---

# Dashboard

> Paths below use `FROM "wiki"`, which assumes you opened the `GenAI-Wiki` folder as the vault root (see [[SETUP]]). If you opened a parent folder instead, change `"wiki"` to `"GenAI-Wiki/wiki"` in each query.

## All pages, newest first

```dataview
TABLE WITHOUT ID file.link AS Page, type AS Type, updated AS Updated
FROM "wiki"
WHERE type != "dashboard"
SORT updated DESC
```

## Concept pages

```dataview
LIST
FROM "wiki"
WHERE type = "concept"
SORT file.name ASC
```

## Comparisons & syntheses

```dataview
LIST
FROM "wiki"
WHERE type = "comparison"
SORT file.name ASC
```

## Sources

```dataview
TABLE WITHOUT ID file.link AS Source, updated AS Added
FROM "wiki/sources"
SORT updated DESC
```

## Pages by tag

```dataview
TABLE WITHOUT ID file.link AS Page, tags AS Tags
FROM "wiki"
WHERE type != "dashboard"
SORT file.name ASC
```
