# Pawtraits Attribution Taxonomy

Use lowercase values and underscores. Do not invent new channel names when an existing one applies.

## Parameters

- `utm_source`: the platform or owned source.
- `utm_medium`: the channel class.
- `utm_campaign`: the initiative or sustained test.
- `utm_content`: the exact creative, article CTA or placement.

## Standard mediums

- `paid_ai`
- `ai_referral`
- `organic_social`
- `paid_social`
- `organic_content`
- `email`
- `referral`

## AI traffic

| Use | Source | Medium | Campaign example | Content example |
| --- | --- | --- | --- | --- |
| ChatGPT Ads | chatgpt | paid_ai | pawtraits_launch | quality_angle_01 |
| Organic ChatGPT link we control | chatgpt | ai_referral | organic_ai | pet_portrait_guide |
| Perplexity | perplexity | ai_referral | organic_ai | pet_portrait_guide |
| Gemini | gemini | ai_referral | organic_ai | pet_portrait_guide |
| Claude | claude | ai_referral | organic_ai | pet_portrait_guide |

## Social

| Platform | Source | Medium |
| --- | --- | --- |
| Threads organic | threads | organic_social |
| Facebook organic | facebook | organic_social |
| Instagram organic | instagram | organic_social |
| Facebook paid | facebook | paid_social |
| Instagram paid | instagram | paid_social |

## Blog

Internal article CTAs use:

- `utm_source=pawtraits_blog`
- `utm_medium=organic_content`
- `utm_campaign=evergreen_blog` or a deliberate editorial campaign
- `utm_content=<article_slug>_<placement>`

Example:

`https://pawtraitsforapound.co.uk/?utm_source=pawtraits_blog&utm_medium=organic_content&utm_campaign=evergreen_blog&utm_content=perfect_pet_photo_bottom_cta#order`

## Rules

1. `source` identifies where the visitor came from. Never put `paid`, `organic` or `ad` into source.
2. `medium` identifies how the traffic was acquired.
3. `campaign` stays stable across a coherent test or initiative.
4. `content` identifies the specific creative or placement.
5. Do not add UTMs to ordinary internal navigation. Use them only where attribution is intentionally being measured, such as article-to-order CTAs.
6. Canonical URLs must never contain UTM parameters.
7. The Pawtraits order ledger is the purchase-attribution source of truth. GA4 is behavioural analytics, not the authoritative order ledger.
