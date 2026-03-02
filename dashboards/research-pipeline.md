---
type: dashboard
status: active
---

# Research Pipeline

Track research from raw input through to codified reference.

---

## All Research by Date

```dataview
TABLE status, source, date
FROM "research"
WHERE !contains(file.path, "_archived")
SORT date DESC
```

## Research by Source

```dataview
TABLE date, status
FROM "research"
WHERE source != null AND !contains(file.path, "_archived")
GROUP BY source
```

## Unlinked Research

Research files not referenced by any decision — might be orphaned or waiting to be processed.

```dataview
TABLE date, source, status
FROM "research"
WHERE !contains(file.path, "_archived")
SORT date DESC
```

## Archived Research

```dataview
TABLE date, source
FROM "research/_archived"
SORT date DESC
```

## Consolidated Research

```dataview
TABLE date, status
FROM "research/consolidated"
SORT date DESC
```
