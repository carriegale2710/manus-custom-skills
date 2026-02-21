# Quick Start Guide

Get your market research report up and running in 6 steps.

## Step 1: Define Your Research Scope

Create a file called `scope.json`:

```json
{
  "problem_space": "Chrome extension micro-SaaS for solo founders",
  "target_founder_profile": {
    "skills": ["UX Designer", "Indie Developer"],
    "neurodivergence": "AuDHD",
    "personality": "INTP"
  },
  "success_metrics": {
    "revenue_target_usd": 2000,
    "revenue_target_local": "2000 AUD",
    "timeline_months": 3,
    "growth_channels": "organic only, no paid ads"
  },
  "ideas_count": 10
}
```

## Step 2: Gather Research Data

Use the `research-template.ts` file to structure your data. Fill in:

- **User Quotes** — Search Reddit communities (r/ADHD, r/UXDesign, r/SaaS) for pain points
- **Market Data** — Find TAM and CAGR from industry reports
- **Competitor Analysis** — Identify 2-3 competitors per idea and their weaknesses
- **SWOT Analysis** — Document strengths, weaknesses, opportunities, threats

Example research workflow:

```bash
# 1. Search Reddit for user pain points
# r/ADHD - "tab hoarding", "context switching", "working memory"
# r/UXDesign - "audit tools", "design system", "accessibility"

# 2. Find market data
# Google: "ADHD apps market size 2024"
# Google: "Chrome extension market CAGR"

# 3. Analyze competitors
# Product Hunt, G2, Capterra, company websites

# 4. Fill in research-template.ts with your findings
```

## Step 3: Calculate Scores

For each idea, score across 5 criteria (1-10 scale):

| Criterion | Weight | How to Score |
|-----------|--------|-------------|
| Market Size | 20% | TAM growth trajectory (larger + faster = higher) |
| PMF Evidence | 30% | User pain intensity from Reddit + competitor revenue |
| Founder Fit | 25% | Alignment with your skills and lived experience |
| Competitor Gap | 15% | Blue ocean opportunity (higher = less competition) |
| Revenue Speed | 10% | Time to $2K MRR without paid ads |

**Formula:**
```
Composite Score = (marketSize × 0.20) + (pmf × 0.30) + (founderFit × 0.25) + (competitorGap × 0.15) + (revenueSpeed × 0.10)
```

## Step 4: Generate Charts

Convert your research data to JSON:

```bash
# Create data.json from your research-template.ts
# Include all ideas, market stats, revenue projections, market growth data

python3 generate-charts.py --input data.json --output ./charts
```

This generates 10 charts:
1. Opportunity Score Ranking
2. Market Sizes
3. SWOT Radar (top 3)
4. Revenue Projection
5. Competitor Gap Matrix
6. Market Growth Trends
7. Founder-Market Fit
8. Pricing vs Users Needed
9. Risk vs Reward Quadrant
10. Market Overview

## Step 5: Compile PDF Report

Create a Markdown file with your findings:

```markdown
# Market Research Report

## Executive Summary
- Problem statement
- Top 3 ideas
- Key findings

## Methodology
- Evaluation criteria
- Data sources
- Founder profile

## Market Context
- Key statistics
- Growth trends

## Ranked Ideas
[For each idea: name, problem, SWOT, competitors, growth channels]

## Comparative Analysis
[Charts and tables comparing all ideas]

## References
[All sources with URLs]
```

Convert to PDF:

```bash
manus-md-to-pdf report.md output/market-research-report.pdf
```

## Step 6: Build Interactive Dashboard

Use the provided dashboard template to create a React web app:

```bash
# Initialize project
manus webdev init-project my-dashboard --scaffold web-static

# Copy your data
cp research-data.ts my-dashboard/client/src/lib/data.ts

# Copy charts
cp charts/*.png my-dashboard/client/public/charts/

# Start dev server
cd my-dashboard
pnpm dev

# Visit http://localhost:3000
```

The dashboard includes:
- Overview with animated stats
- Filterable/sortable idea cards
- Interactive Recharts visualizations
- SWOT radar charts
- Revenue projections
- References section

---

## Common Mistakes to Avoid

❌ **Mistake 1:** Scoring ideas without real user validation
- ✅ **Fix:** Always include Reddit quotes and willingness-to-pay signals

❌ **Mistake 2:** Ignoring founder-market fit
- ✅ **Fix:** Score founder fit separately; it's 25% of the composite score

❌ **Mistake 3:** Using generic competitor analysis
- ✅ **Fix:** For each competitor, identify specifically WHY your idea is different

❌ **Mistake 4:** Overestimating revenue speed
- ✅ **Fix:** Use conservative assumptions; most ideas take 4-6 months to $2K MRR

❌ **Mistake 5:** Skipping citations
- ✅ **Fix:** Every statistic needs a source URL; this builds credibility

---

## Tips for Success

💡 **Tip 1:** Start with 5-10 ideas, not 50
- Easier to research deeply
- Easier to compare fairly
- Better decision-making

💡 **Tip 2:** Weight criteria based on YOUR priorities
- If you're ADHD-focused, increase founderFit weight to 35%
- If you're risk-averse, increase competitorGap weight to 25%

💡 **Tip 3:** Use the "would you pay for this?" test
- Post mockups in relevant Reddit communities
- Ask directly: "Would you pay $7/month for this?"
- Look for "instant buy" signals

💡 **Tip 4:** Validate your #1 pick before building
- Spend 48 hours getting user feedback
- Aim for 50+ responses to a "would you pay" poll
- Adjust your idea based on feedback

💡 **Tip 5:** Share your report with potential co-founders
- Use the interactive dashboard to get feedback
- Let them re-weight criteria to see how rankings change
- Builds alignment on strategy

---

## Next Steps After Report

1. **Validate your #1 idea** (48 hours)
   - Post in r/ADHD, r/UXDesign, relevant communities
   - Get 50+ responses to "would you pay for this?"
   - Collect feature requests and pain points

2. **Build MVP** (4 weeks)
   - Focus on core problem only
   - Launch on Product Hunt
   - Get first 100 users

3. **Iterate based on feedback** (ongoing)
   - Track which features users actually use
   - Adjust pricing based on willingness to pay
   - Grow organically through word-of-mouth

4. **Track progress** (monthly)
   - Monitor MRR growth vs. projections
   - Update dashboard with real data
   - Share progress with community

---

## Resources

- **Market Data:** Market.us, HTF Intelligence, Exactitude Consultancy
- **User Research:** Reddit, Twitter/X, Indie Hackers
- **Competitor Data:** Product Hunt, G2, Capterra
- **Revenue Data:** Indie Hackers case studies, Twitter/X founder posts
- **Tools:** Python (matplotlib, seaborn), React (Recharts), Tailwind CSS

---

**Ready to start?** Begin with Step 1 above, and reach out if you hit any blockers!
