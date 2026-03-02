---
type: dashboard
status: active
---

# Content Tracker

Track content from draft through to published with engagement data.

---

## Drafts (Ready to Post)

```dataview
TABLE platform, type, pillar, date
FROM "content/drafts"
SORT date DESC
```

## Scheduled

```dataview
TABLE platform, type, date
FROM "content/scheduled"
SORT date DESC
```

## Published

```dataview
TABLE platform, type, date
FROM "content/published"
SORT date DESC
```

## Content by Platform

```dataview
TABLE date, type, status
FROM "content"
WHERE platform != null
GROUP BY platform
```

## Content by Pillar

```dataview
TABLE date, platform
FROM "content"
WHERE pillar != null
GROUP BY pillar
```
