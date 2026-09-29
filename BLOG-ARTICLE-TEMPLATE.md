# Pawtraits Blog Article Template

Use this document as the structural checklist for every article published under `/blog/<slug>/`.

## Head

- Title: `<Article title> | Pawtraits for a Pound`
- Meta description
- Canonical URL
- `index,follow`
- Open Graph title, description, URL and image
- Pawtraits favicon and shared stylesheet
- Existing Google Analytics Consent Mode block
- `BlogPosting` JSON-LD

## Visible structure

- Standard Pawtraits header navigation
- Breadcrumbs: Home > Blog > Article
- Category eyebrow
- One H1
- Published and updated dates
- Main article inside `.article-prose`
- Useful contextual Pawtraits CTA, not a forced sales insertion
- Related articles when at least two relevant posts exist
- Standard footer, social links and cookie settings

## Search and publishing

- Add a card to `/blog/index.html`
- Add the canonical article URL to `/sitemap.xml`
- Update `dateModified` when making substantive changes
- Validate structured data and internal links
- Confirm there are no em dashes
- Commit and push to `main`
- Verify the GitHub Actions deployment and live URL
