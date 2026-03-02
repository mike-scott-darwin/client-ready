---
type: dashboard
status: active
---

# Dashboard

Central hub for navigating the Client Ready vault.

---

## Quick Links

- [[decisions]] — All decisions by date and status
- [[research-pipeline]] — Research files and where they landed
- [[reference-map]] — Core reference files at a glance
- [[vault-health]] — Broken links, orphans, frontmatter issues
- [[content-tracker]] — Content pipeline status

---

## Recent Decisions

```dataview
TABLE status, date
FROM "decisions"
SORT date DESC
LIMIT 10
```

## Active Research

```dataview
TABLE status, source, date
FROM "research"
WHERE status = "active" OR status = "draft"
SORT date DESC
LIMIT 10
```

## Recent Outputs

```dataview
TABLE type, status, date
FROM "outputs"
WHERE date != null
SORT date DESC
LIMIT 10
```
