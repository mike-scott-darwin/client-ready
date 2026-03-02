---
type: dashboard
status: active
---

# Reference Map

All reference files that inform outputs. These are the source of truth.

---

## Core (Required)

```dataview
TABLE status, date, file.size AS "Size"
FROM "reference/core"
SORT file.name ASC
```

## Proof

```dataview
TABLE status, date
FROM "reference/proof"
SORT file.name ASC
```

## Angles

```dataview
TABLE status, date
FROM "reference/proof/angles"
SORT file.name ASC
```

## Domain

```dataview
TABLE status, date
FROM "reference/domain"
WHERE !contains(file.path, "classroom") AND !contains(file.path, "funnel")
SORT file.name ASC
```

## Domain — Classroom

```dataview
TABLE status, date
FROM "reference/domain/classroom"
SORT file.name ASC
```

## Domain — Funnel

```dataview
TABLE status, date
FROM "reference/domain/funnel"
SORT file.name ASC
```

## Brand

```dataview
TABLE status, date
FROM "reference/brand"
SORT file.name ASC
```
