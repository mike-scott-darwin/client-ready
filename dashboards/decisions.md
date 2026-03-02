---
type: dashboard
status: active
---

# Decisions

All decisions sorted by date. Click any row to open the full decision file.

---

## All Decisions

```dataview
TABLE status, date, file.size AS "Size"
FROM "decisions"
SORT date DESC
```

## Active Decisions

```dataview
TABLE date
FROM "decisions"
WHERE status = "active"
SORT date DESC
```

## Decisions Without Linked Research

Decisions that don't reference their source research — potential gaps.

```dataview
TABLE date, status
FROM "decisions"
WHERE !linked_research OR length(linked_research) = 0
SORT date DESC
```
