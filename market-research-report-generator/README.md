# Market Research Report Generator Skill

A comprehensive, reusable skill for generating data-driven market research reports with SWOT analysis, competitor gap analysis, professional PDF documentation, and interactive web dashboards.

## 📋 What's Included

- **SKILL.md** — Complete 6-phase workflow documentation with best practices
- **QUICKSTART.md** — Get started in 6 steps
- **skill.json** — Metadata and skill configuration
- **research-template.ts** — TypeScript template for structuring research data
- **generate-charts.py** — Python script to generate 10 publication-ready charts
- **README.md** — This file

## 🎯 Use Cases

- ✅ Validate 5-15 business ideas before building
- ✅ Rank opportunities by weighted criteria (market size, PMF, founder fit, etc.)
- ✅ Create investor pitch decks with data-driven insights
- ✅ Competitive analysis and market sizing
- ✅ Product strategy and roadmapping
- ✅ Founder-market fit assessment
- ✅ Team alignment on product decisions

## 🚀 Quick Start

### 1. Read the Documentation

Start with **QUICKSTART.md** for a 6-step overview, or read **SKILL.md** for comprehensive details.

### 2. Define Your Scope

```json
{
  "problem_space": "Your market",
  "target_founder_profile": { "skills": [...], "goals": [...] },
  "success_metrics": { "revenue_target": 2000, "timeline_months": 3 },
  "ideas_count": 10
}
```

### 3. Gather Research Data

Use `research-template.ts` to structure:
- User quotes from Reddit/Twitter
- Market statistics and CAGR
- Competitor analysis
- SWOT assessments

### 4. Generate Charts

```bash
python3 generate-charts.py --input data.json --output ./charts
```

Generates 10 charts:
1. Opportunity Score Ranking
2. Market Sizes
3. SWOT Radar
4. Revenue Projection
5. Competitor Gap Matrix
6. Market Growth Trends
7. Founder-Market Fit
8. Pricing vs Users Needed
9. Risk vs Reward Quadrant
10. Market Overview

### 5. Compile PDF Report

```bash
manus-md-to-pdf report.md output/market-research-report.pdf
```

### 6. Build Interactive Dashboard

Use the provided React template to create an interactive web dashboard with:
- Filterable/sortable idea cards
- Interactive Recharts visualizations
- SWOT radar charts per idea
- Revenue projections
- References section

## 📊 Evaluation Methodology

Each idea is scored across 5 weighted criteria (1-10 scale):

| Criterion | Weight | Definition |
|-----------|--------|-----------|
| Market Size | 20% | TAM and CAGR growth trajectory |
| PMF Evidence | 30% | User pain intensity + competitor revenue proof |
| Founder Fit | 25% | Alignment with your skills and lived experience |
| Competitor Gap | 15% | Blue ocean opportunity vs. existing solutions |
| Revenue Speed | 10% | Time to revenue target without paid ads |

**Composite Score = (marketSize × 0.20) + (pmf × 0.30) + (founderFit × 0.25) + (competitorGap × 0.15) + (revenueSpeed × 0.10)**

## 🎨 Design Philosophy

The skill emphasizes:
- **Data-Driven Decisions** — Every claim backed by sources and user quotes
- **Founder-Market Fit** — Tailored to your unique strengths and constraints
- **Transparency** — Clear methodology and weighted criteria
- **Professionalism** — Publication-ready charts and reports
- **Interactivity** — Explore data yourself, not just read conclusions

## 📁 File Structure

```
market-research-report-generator/
├── SKILL.md                    # Complete documentation (6 phases, best practices)
├── QUICKSTART.md               # 6-step quick start guide
├── README.md                   # This file
├── skill.json                  # Metadata and configuration
├── research-template.ts        # TypeScript data structure + helpers
└── generate-charts.py          # Python script for chart generation
```

## 🛠️ Requirements

### For Chart Generation
```bash
pip install matplotlib seaborn plotly pandas numpy
```

### For PDF Report
```bash
# Use manus-md-to-pdf utility (pre-installed)
manus-md-to-pdf report.md output.pdf
```

### For Interactive Dashboard
- React 19 + TypeScript
- Recharts (for interactive charts)
- Tailwind CSS 4
- Framer Motion (for animations)

## 💡 Key Features

### 1. Weighted Scoring System
- Customize weights based on your priorities
- Transparent methodology
- Reproducible results

### 2. User Validation
- Real quotes from Reddit, Twitter, LinkedIn
- Willingness-to-pay signals
- Competitor revenue proof

### 3. SWOT Analysis
- Structured assessment per idea
- Competitor gap identification
- Risk and opportunity mapping

### 4. Revenue Modeling
- Conservative/realistic/optimistic scenarios
- Users needed for revenue target
- Pricing strategy comparison

### 5. Market Intelligence
- TAM sizing and CAGR
- Growth trends (2024-2030)
- Regulatory tailwinds

### 6. Professional Output
- 10 publication-ready charts (300 DPI)
- 15-25 page PDF report
- Interactive web dashboard
- Clickable references

## 📈 Output Examples

### PDF Report Includes
- Executive summary with top 3 ideas
- Methodology and evaluation criteria
- Market context and statistics
- Per-idea analysis (1-2 pages each)
- Comparative analysis with charts
- Strategic recommendations
- Full references with URLs

### Interactive Dashboard Includes
- Overview with animated stat counters
- Filterable/sortable idea cards
- Per-idea detail panels with SWOT radar
- Interactive Recharts visualizations
- Revenue projection scenarios
- Risk vs reward quadrant
- Full comparison table
- References section

## 🎓 Learning Resources

- **Market Sizing:** "Nail It Then Scale It" by Nathan Furr & Paul Ahlstrom
- **Founder-Market Fit:** "The Mom Test" by Rob Fitzpatrick
- **SWOT Analysis:** "Competitive Strategy" by Michael Porter
- **Data Visualization:** "Storytelling with Data" by Cole Nussbaumer Knaflic
- **Indie SaaS:** Indie Hackers (indiehackers.com) — real revenue data

## ❓ FAQ

**Q: How long does a complete report take?**
A: 40-60 hours (research + analysis + dashboard). You can speed this up by:
- Focusing on 5-10 ideas instead of 15
- Using existing market research reports
- Automating chart generation with the Python script

**Q: Can I customize the evaluation criteria?**
A: Yes! The skill is designed to be flexible. Adjust the weights in the scoring formula based on your priorities.

**Q: What if I only need a PDF report, not a dashboard?**
A: You can skip the dashboard step. The PDF report is standalone and complete.

**Q: Can I use this for other business types (not just micro-SaaS)?**
A: Absolutely! The methodology works for any business idea evaluation. Just adjust the criteria and data sources to match your context.

**Q: How do I validate my top idea?**
A: Post a "would you pay for this?" poll in relevant communities (Reddit, Twitter) with a mockup. Aim for 50+ responses. Look for "instant buy" signals.

## 🔄 Continuous Improvement

This skill is designed to evolve based on real-world usage. If you:
- Discover a better data source
- Develop a new evaluation criterion
- Create a useful visualization
- Have feedback on the methodology

**Please share it back!** The skill improves when informed by actual usage.

## 📞 Support

For questions or issues:
1. Check **SKILL.md** for comprehensive documentation
2. Review **QUICKSTART.md** for common patterns
3. Look at the **research-template.ts** for data structure examples
4. Run the Python script with `--help` flag for options

## 📄 License

MIT — Free to use and modify

## 🙏 Acknowledgments

This skill was developed based on real-world market research for validating 10 Chrome extension micro-SaaS ideas. It incorporates best practices from:
- Design thinking and SWOT analysis
- Lean startup methodology
- Data-driven decision making
- Professional report writing
- Interactive data visualization

---

**Version:** 1.0.0  
**Created:** February 2026  
**Maintained By:** Manus AI
