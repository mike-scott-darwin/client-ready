---
type: dashboard
status: active
date: 2026-03-02
---

# Vault Health

Last sweep: 2026-03-02

---

## Files Without Frontmatter

```dataview
LIST
FROM ""
WHERE !type AND !contains(file.path, "dashboards") AND !contains(file.path, ".obsidian") AND !contains(file.path, "canvas")
SORT file.path ASC
```

## Files Missing Status

```dataview
TABLE type, date
FROM ""
WHERE type != null AND !status
SORT file.path ASC
```

## Files Missing Date

```dataview
TABLE type, status
FROM ""
WHERE type != null AND !date AND !contains(file.path, "dashboards")
SORT file.path ASC
```

---

## Known Issues (2026-03-02 Sweep)

### Broken Links (28)

Mostly decision files pointing to research that moved to _archived/:
- 22 links in 6 decision files point to old research paths
- 4 links in email outputs reference classroom downloads not yet created
- 1 decision links to a non-existent sibling decision
- 1 link points to a renamed file

### Orphan Files (94)

Files with zero incoming links:
- 14 decision files never referenced by other files
- 22+ research files (including crystallize logs and triage notes)
- 33 output files (mostly sprint-docs with no incoming links)
- 15 reference files (classroom downloads, delivery docs)

### Frontmatter Parse Errors (6)

Ad output files with unquoted colons in review_status YAML values:
- before-the-funnel.md, clarity-unlock.md, content-merry-go-round.md
- 3 archived ad batch files

### Potential Duplicates (7 pairs)

Same filename in different directories — check if one copy is redundant:
- outputs/ads/ vs reference/proof/angles/ (4 angle files exist in both)
- outputs/pages/ vs outputs/products/ (3 bump files exist in both)
