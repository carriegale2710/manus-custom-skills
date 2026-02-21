# Market Research Report Generator Skill

**Version:** 1.0.0  
**Created:** February 2026  
**Purpose:** Generate comprehensive, data-driven market research reports with SWOT analysis, competitor gap analysis, PDF documentation, and interactive web dashboards.

---

## Overview

This skill automates the end-to-end process of creating a professional market research report with:

1. **Research Phase** — Gather user pain points from social media (Reddit, Twitter), market statistics from industry reports, and competitor analysis
2. **Analysis Phase** — Rank opportunities using weighted scoring (market size, PMF evidence, founder fit, competitor gap, revenue speed)
3. **Visualization Phase** — Generate publication-ready charts (bar, line, scatter, radar, heatmap)
4. **Report Generation** — Compile findings into a professional PDF with citations and references
5. **Interactive Dashboard** — Build a React + Recharts web dashboard for data exploration

**Ideal for:**
- Validating business ideas before building
- Competitive analysis and market sizing
- Investor pitch decks and due diligence
- Product strategy and roadmapping
- Founder-market fit assessment

---

## When to Use This Skill

✅ **Use this skill when:**
- You need to validate 5-15 business ideas or product concepts
- You want to rank opportunities by multiple weighted criteria
- You need both a PDF report and an interactive web dashboard
- You're targeting a specific founder profile or market segment
- You want to include real user quotes and verified market data
- You need to create a professional, data-driven narrative

❌ **Don't use this skill when:**
- You only need a simple comparison table (use a spreadsheet instead)
- You need real-time data from APIs (this skill uses static research)
- You're analyzing 50+ ideas (too many for effective comparison)
- You need deep technical due diligence (this is market-level analysis only)

---

## Workflow

### Phase 1: Define Your Research Scope

**Input:** Your research question and target audience

```
Example: "Find 10 validated Chrome extension micro-SaaS ideas for a UX designer / indie dev / AuDHD founder targeting $2K AUD MRR in 3 months"
```

**Deliverable:** A clear problem statement and evaluation criteria

**Steps:**
1. Define the problem space (e.g., "Chrome extension micro-SaaS for solo founders")
2. Identify your target founder profile (e.g., "UX designer, indie dev, neurodivergent, INTP")
3. Set success metrics (e.g., "$2K AUD MRR in 3 months, no paid ads")
4. Determine number of ideas to research (5-15 recommended)
5. List evaluation criteria (e.g., market size, PMF evidence, founder fit, competitor gap, revenue speed)

---

### Phase 2: Research & Gather Data

**Input:** Your defined scope and evaluation criteria

**Deliverable:** Structured data file with all ideas, user quotes, market stats, and competitor info

**Steps:**

1. **Social Media Research** (Reddit, Twitter/X, LinkedIn)
   - Search for user pain points in relevant communities (r/ADHD, r/UXDesign, r/SaaS, etc.)
   - Capture direct user quotes with source URLs
   - Document sentiment and frequency of pain mentions
   - Look for "would pay for this" signals

2. **Market Data Collection**
   - Find TAM (Total Addressable Market) from industry reports
   - Document CAGR (Compound Annual Growth Rate)
   - Collect competitor pricing and feature sets
   - Note market trends and regulatory tailwinds

3. **Competitor Analysis**
   - Identify 2-3 direct competitors per idea
   - Document their weaknesses and gaps
   - Find their pricing and revenue (if public)
   - Identify unmet needs they're missing

4. **Founder-Market Fit Assessment**
   - Rate alignment with your founder profile (1-10 scale)
   - Consider lived experience advantages
   - Evaluate skill requirements vs. existing capabilities
   - Assess passion/authenticity fit

**Output Format:** TypeScript data structure (see `data.ts` template)

```typescript
interface Idea {
  rank: number;
  id: string;
  name: string;
  tagline: string;
  score: number; // 1-10 composite score
  category: string;
  marketSize: string; // e.g., "$1.79B"
  cagr: string; // e.g., "11.9%"
  pricing: number; // USD/month
  usersNeeded: number; // to hit revenue target
  problem: string; // 2-3 sentence problem statement
  userQuotes: Array<{ text: string; source: string; url: string }>;
  competitors: Array<{ name: string; weakness: string }>;
  swot: {
    strengths: string[];
    weaknesses: string[];
    opportunities: string[];
    threats: string[];
  };
  scores: {
    marketSize: number;
    pmf: number;
    founderFit: number;
    competitorGap: number;
    revenueSpeed: number;
  };
}
```

---

### Phase 3: Analyze & Rank Ideas

**Input:** Structured research data from Phase 2

**Deliverable:** Ranked list with composite opportunity scores

**Scoring Methodology:**

Each idea is scored across 5 weighted criteria (1-10 scale):

| Criterion | Weight | Definition |
|-----------|--------|-----------|
| Market Size | 20% | TAM growth trajectory and CAGR |
| PMF Evidence | 30% | User pain intensity from social media + competitor revenue proof |
| Founder Fit | 25% | Alignment with your skills, lived experience, and passion |
| Competitor Gap | 15% | Blue ocean opportunity vs. existing solutions |
| Revenue Speed | 10% | Time to revenue target without paid ads |

**Formula:**
```
Composite Score = (marketSize × 0.20) + (pmf × 0.30) + (founderFit × 0.25) + (competitorGap × 0.15) + (revenueSpeed × 0.10)
```

**SWOT Analysis Template:**

For each idea, document:
- **Strengths** — Competitive advantages, founder expertise, market timing
- **Weaknesses** — Technical complexity, behavior change required, market risks
- **Opportunities** — Regulatory tailwinds, market growth, adjacent markets
- **Threats** — Big players entering, free alternatives, platform policy changes

**Competitor Gap Analysis:**

For each competitor, identify:
- What they do well (their moat)
- What they're missing (your opportunity)
- Why they haven't solved it (technical, business model, or market reasons)

---

### Phase 4: Generate Visualizations

**Input:** Ranked ideas and analysis data

**Deliverable:** 10 publication-ready charts (PNG format)

**Recommended Charts:**

1. **Opportunity Score Ranking** (Horizontal Bar Chart)
   - X-axis: Composite score (0-10)
   - Y-axis: Idea names
   - Color-coded by category

2. **Market Sizes** (Vertical Bar Chart)
   - X-axis: Ideas
   - Y-axis: Market size (USD billions)
   - Sorted by size

3. **SWOT Radar** (Radar Chart for top 3 ideas)
   - 5 axes: Strengths, Weaknesses, Opportunities, Threats, Founder Fit
   - One polygon per idea

4. **Revenue Projection** (Line Chart)
   - X-axis: Months (0-6)
   - Y-axis: MRR (USD or local currency)
   - 3 lines: Conservative, Realistic, Optimistic

5. **Competitor Gap Matrix** (Heatmap)
   - X-axis: Ideas
   - Y-axis: Competitor gap score (1-5)
   - Color intensity: Gap opportunity

6. **Market Growth Trends** (Multi-line Chart)
   - X-axis: Years (2024-2030)
   - Y-axis: Market size (USD billions)
   - Lines: Key market segments

7. **Founder-Market Fit** (Grouped Bar Chart)
   - X-axis: Top 5 ideas
   - Y-axis: Fit score (1-10)
   - Grouped bars: UX Designer, ADHD, Indie Dev

8. **Pricing vs. Users Needed** (Scatter Plot)
   - X-axis: Monthly price (USD)
   - Y-axis: Users needed for revenue target
   - Bubble size: Market size

9. **Risk vs. Reward** (Scatter Plot)
   - X-axis: Risk score (1-10)
   - Y-axis: Opportunity score (1-10)
   - Bubble size: MRR potential
   - Color: Category

10. **Market Overview** (Summary Infographic)
    - Key statistics (market size, CAGR, user base, revenue targets)
    - Animated counters for impact

**Tools:**
- Python: matplotlib, seaborn, plotly for static charts
- JavaScript: Recharts for interactive web charts
- Design: Use consistent color palette, professional typography, clear legends

---

### Phase 5: Compile PDF Report

**Input:** All research, analysis, visualizations, and citations

**Deliverable:** Professional PDF report (15-25 pages)

**Report Structure:**

```
1. Executive Summary (1 page)
   - Problem statement
   - Top 3 ideas with scores
   - Key findings and recommendations

2. Methodology (1 page)
   - Evaluation criteria and weights
   - Data sources and validation approach
   - Founder profile and success metrics

3. Market Context (2 pages)
   - Key statistics and market size data
   - Growth trends and tailwinds
   - Competitive landscape overview

4. Ranked Ideas (8-12 pages, 1-2 per idea)
   For each idea:
   - Name, tagline, opportunity score
   - Problem statement with user quotes
   - Market size and pricing model
   - SWOT analysis (table or diagram)
   - Competitor gap analysis
   - Growth channels and revenue path
   - Risk assessment

5. Comparative Analysis (3-4 pages)
   - Opportunity score ranking chart
   - Risk vs. reward quadrant
   - Founder-market fit comparison
   - Pricing and revenue model comparison
   - Market growth projections

6. Strategic Recommendations (1 page)
   - Top 3 ideas ranked
   - Validation next steps
   - Timeline to revenue target
   - Key success factors

7. References (1 page)
   - All cited sources with URLs
   - Data sources and methodology notes
```

**Tools:**
- Use `manus-md-to-pdf` utility to convert Markdown → PDF
- Or use Python fpdf2/reportlab for programmatic PDF generation
- Embed all charts as high-resolution images (300 DPI)
- Include clickable table of contents and page numbers

---

### Phase 6: Build Interactive Dashboard

**Input:** All research data, visualizations, and analysis

**Deliverable:** React web app with Recharts visualizations

**Dashboard Features:**

1. **Navigation**
   - Sticky header with section tabs (Overview, Ideas, Analysis, Projections, References)
   - Mobile-responsive hamburger menu

2. **Overview Section**
   - Hero headline and problem statement
   - Animated market stat counters
   - Top 3 ideas quick view
   - Methodology breakdown

3. **Ideas Section**
   - Filterable/sortable idea cards (by rank, market size, risk)
   - Category filters
   - Per-idea detail panel with:
     - SWOT radar chart
     - User quotes with source links
     - Competitor gap analysis
     - Growth channels
     - Key metrics

4. **Analysis Section**
   - Opportunity score ranking (bar chart)
   - Risk vs. reward scatter plot
   - Founder-market fit comparison
   - Competitor gap matrix
   - Full comparison table

5. **Projections Section**
   - 6-month MRR scenarios (line chart)
   - Market growth trends (multi-line chart)
   - Revenue path breakdown (timeline)

6. **References Section**
   - All sources with clickable links
   - Methodology notes

**Design:**
- Dark mode dashboard (navy/slate base, indigo accents)
- Consistent color coding by category
- Smooth animations and transitions
- Mobile-responsive grid layout
- Accessible contrast ratios and keyboard navigation

**Tech Stack:**
- React 19 + TypeScript
- Recharts for interactive charts
- Tailwind CSS 4 for styling
- Framer Motion for animations
- Wouter for client-side routing

---

## Implementation Steps

### Step 1: Set Up Your Research Environment

```bash
# Create project directory
mkdir -p ~/my-market-research && cd ~/my-market-research

# Create subdirectories
mkdir -p research/{raw,processed} charts output
```

### Step 2: Define Your Scope

Create a `scope.md` file:

```markdown
# Research Scope

## Problem Space
[Your problem statement]

## Target Founder Profile
- Skills: [e.g., UX Designer, Indie Dev]
- Neurodivergence: [e.g., AuDHD, INTP]
- Goals: [e.g., $2K AUD MRR in 3 months]

## Success Metrics
- Revenue target: [e.g., $2,000 AUD MRR]
- Timeline: [e.g., 3 months]
- Growth channels: [e.g., organic only, no paid ads]

## Evaluation Criteria
1. Market Size (20%)
2. PMF Evidence (30%)
3. Founder Fit (25%)
4. Competitor Gap (15%)
5. Revenue Speed (10%)

## Ideas to Research
[List 5-15 ideas]
```

### Step 3: Gather Research Data

Use the provided `research-template.ts` to structure your data:

```typescript
// research/processed/ideas.ts
import { Idea } from './types';

export const IDEAS: Idea[] = [
  {
    rank: 1,
    id: "idea-1",
    name: "Your Idea Name",
    tagline: "One-line description",
    score: 0, // Will be calculated
    category: "Category Name",
    marketSize: "$1.5B",
    cagr: "15.2%",
    pricing: 9,
    usersNeeded: 222,
    problem: "Problem statement...",
    userQuotes: [
      { text: "User quote", source: "Reddit r/community", url: "https://..." }
    ],
    competitors: [
      { name: "Competitor", weakness: "Missing feature X" }
    ],
    swot: {
      strengths: ["..."],
      weaknesses: ["..."],
      opportunities: ["..."],
      threats: ["..."]
    },
    scores: {
      marketSize: 8,
      pmf: 9,
      founderFit: 8,
      competitorGap: 8,
      revenueSpeed: 9
    }
  }
];
```

### Step 4: Generate Visualizations

Use the provided `generate-charts.py` script:

```bash
python3 generate-charts.py \
  --input research/processed/ideas.ts \
  --output charts/ \
  --style professional
```

Or use the Recharts library in your React dashboard for interactive charts.

### Step 5: Compile PDF Report

```bash
# Using Markdown → PDF conversion
manus-md-to-pdf research/report.md output/market-research-report.pdf

# Or use Python for programmatic generation
python3 generate-pdf.py \
  --ideas research/processed/ideas.ts \
  --charts charts/ \
  --output output/market-research-report.pdf
```

### Step 6: Build Interactive Dashboard

```bash
# Initialize web project
manus webdev init-project my-dashboard --scaffold web-static

# Copy data and components
cp research/processed/ideas.ts my-dashboard/client/src/lib/data.ts
cp charts/*.png my-dashboard/client/public/charts/

# Build and deploy
cd my-dashboard
pnpm dev
# Visit http://localhost:3000
```

---

## Templates & Resources

### Template Files

1. **research-template.ts** — TypeScript interface for structuring research data
2. **generate-charts.py** — Python script to generate all 10 charts
3. **generate-pdf.py** — Python script to compile PDF report
4. **dashboard-template.tsx** — React component template for interactive dashboard
5. **data-template.ts** — Sample data structure with all fields

### Color Palette (Recommended)

```css
--indigo: #6366F1;      /* Primary accent */
--emerald: #10B981;     /* Positive metrics */
--rose: #F43F5E;        /* Risk/warnings */
--amber: #F59E0B;       /* Neutral/secondary */
--violet: #8B5CF6;      /* Tertiary */
--cyan: #06B6D4;        /* Quaternary */
```

### Sample Data Sources

- **Market Size:** HTF Market Intelligence, Market.us, Exactitude Consultancy
- **User Quotes:** Reddit (r/ADHD, r/UXDesign, r/SaaS), Twitter/X, LinkedIn
- **Competitor Data:** Product Hunt, G2, Capterra, company websites
- **Revenue Data:** Indie Hackers, Twitter/X founder posts, case studies

---

## Common Patterns & Best Practices

### Pattern 1: Founder-Market Fit Scoring

Assess alignment across three dimensions:

```typescript
founderFit: {
  ux: 8,      // UX Designer skills alignment (1-10)
  adhd: 10,   // ADHD lived experience (1-10)
  dev: 8      // Indie dev capability (1-10)
}
```

**Calculation:** Average of the three scores, weighted toward your strongest areas.

### Pattern 2: User Quote Validation

Always include:
- Direct quote (in quotes)
- Source (subreddit, Twitter handle, publication)
- URL (clickable link for verification)

```typescript
userQuotes: [
  {
    text: "I had 7,000+ tabs open and couldn't find anything",
    source: "u/bigblackglock17, r/ADHD",
    url: "https://reddit.com/r/ADHD/comments/..."
  }
]
```

### Pattern 3: Competitor Gap Analysis

For each competitor, identify:

```typescript
competitors: [
  {
    name: "Existing Tool",
    weakness: "Saves tabs but doesn't capture intent or address ADHD-specific UX"
  }
]
```

The weakness should highlight **why your idea is different**, not just what they're missing.

### Pattern 4: Revenue Path Calculation

```
Users Needed = Target MRR / (Monthly Price × Conversion Rate)

Example:
- Target: $2,000 AUD MRR
- Price: $7/month
- Conversion Rate: 1% (conservative)
- Users Needed = $2,000 / ($7 × 0.01) = ~286 paying users
```

### Pattern 5: Risk Scoring

Assess risk across multiple dimensions:

```typescript
risk: 3, // 1-10 scale

// Breakdown:
// 1-2: Low risk (proven market, founder expertise, clear path)
// 3-5: Medium risk (some unknowns, execution dependent)
// 6-8: High risk (new market, complex build, behavior change required)
// 9-10: Very high risk (unproven, technical complexity, regulatory)
```

---

## Troubleshooting

### Issue: Low PMF scores despite large market

**Cause:** Market size ≠ PMF evidence. A large market doesn't mean users will pay.

**Solution:** Look for:
- Frequency of pain mentions on social media
- Willingness-to-pay signals ("I would pay for this")
- Competitor revenue proof (e.g., "Making $100K/month")
- Regulatory tailwinds (e.g., ADA lawsuits increasing)

### Issue: Founder fit score seems arbitrary

**Cause:** Founder fit is subjective and context-dependent.

**Solution:** Score based on:
- Lived experience (e.g., ADHD founder building ADHD tools = +2)
- Existing skills (e.g., UX designer building UX tools = +2)
- Passion level (e.g., "I would build this anyway" = +1)
- Time to competency (e.g., "I can learn this in 2 weeks" = +1)

### Issue: Dashboard charts not rendering

**Cause:** Data format mismatch or missing dependencies.

**Solution:**
- Verify data structure matches Recharts expected format
- Check that all required fields are present (no undefined values)
- Run `pnpm install` to ensure recharts and framer-motion are installed
- Test with sample data first

### Issue: PDF report looks unprofessional

**Cause:** Poor image quality, inconsistent formatting, or missing citations.

**Solution:**
- Export charts at 300 DPI (high resolution)
- Use consistent fonts and spacing throughout
- Include all citations with clickable URLs
- Use professional color palette (avoid neon or clashing colors)
- Add page numbers and table of contents

---

## Advanced Customizations

### Customization 1: Add Weighted Scoring by Founder Profile

Allow different founder profiles to weight criteria differently:

```typescript
const weights = {
  "ux-designer": { marketSize: 0.15, pmf: 0.35, founderFit: 0.30, competitorGap: 0.15, revenueSpeed: 0.05 },
  "indie-dev": { marketSize: 0.20, pmf: 0.25, founderFit: 0.20, competitorGap: 0.20, revenueSpeed: 0.15 },
  "neurodivergent": { marketSize: 0.20, pmf: 0.30, founderFit: 0.35, competitorGap: 0.10, revenueSpeed: 0.05 }
};
```

### Customization 2: Add Real-Time Data Integration

Connect to live APIs for:
- Stock market data (for public competitor valuations)
- Reddit API (for live sentiment analysis)
- Google Trends (for search volume trends)
- Crunchbase (for funding and revenue data)

### Customization 3: Add Scenario Planning

Build interactive "what-if" scenarios:
- "What if I charge $15/month instead of $9?"
- "What if I reach 1% conversion rate instead of 0.5%?"
- "What if I grow 20% month-over-month?"

### Customization 4: Add Comparison Mode

Allow side-by-side comparison of 2-3 ideas:
- SWOT comparison
- Pricing comparison
- Timeline comparison
- Risk assessment comparison

---

## Success Metrics

Your research report is successful if:

✅ **Clarity:** Anyone reading it understands why you ranked ideas in that order  
✅ **Validation:** Every claim is backed by a source or user quote  
✅ **Actionability:** Clear next steps for validating your top choice  
✅ **Founder Fit:** The analysis reflects your unique strengths and constraints  
✅ **Professionalism:** The report looks polished and credible (for investors/partners)  
✅ **Interactivity:** The dashboard lets users explore and re-sort ideas themselves  

---

## Example Use Cases

### Use Case 1: Validating a Startup Idea

**Input:** 10 potential micro-SaaS ideas  
**Output:** Ranked list with SWOT analysis and 6-month revenue projections  
**Outcome:** Founder chooses #1 idea, validates with 50 Reddit users, builds MVP in 4 weeks

### Use Case 2: Investor Pitch Deck

**Input:** Your research report and dashboard  
**Output:** PDF report + interactive web dashboard  
**Outcome:** Investor can explore data themselves, increases credibility and engagement

### Use Case 3: Team Alignment

**Input:** 5 product ideas the team is considering  
**Output:** Shared dashboard with transparent scoring methodology  
**Outcome:** Team debates criteria weights, not individual opinions; faster consensus

### Use Case 4: Market Entry Strategy

**Input:** 3 adjacent markets you could expand into  
**Output:** Comparative analysis with market size, competition, and founder fit  
**Outcome:** Data-driven decision on which market to prioritize

---

## References & Further Reading

- **Market Sizing:** "Nail It Then Scale It" by Nathan Furr & Paul Ahlstrom
- **Founder-Market Fit:** "The Mom Test" by Rob Fitzpatrick
- **SWOT Analysis:** "Competitive Strategy" by Michael Porter
- **Data Visualization:** "Storytelling with Data" by Cole Nussbaumer Knaflic
- **Indie SaaS:** Indie Hackers (indiehackers.com) — real revenue data and case studies

---

## Support & Feedback

This skill is designed to be iterated on based on user feedback. If you:

- Find a better data source for market sizing
- Discover a new evaluation criterion that's important
- Build a custom visualization that works well
- Have a different founder profile that needs adjusted weighting

**Please share it back!** The skill improves when real-world usage informs the process.

---

**Last Updated:** February 2026  
**Maintained By:** Manus AI  
**License:** MIT (free to use and modify)
