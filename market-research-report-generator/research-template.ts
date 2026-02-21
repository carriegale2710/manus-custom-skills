/**
 * Market Research Report Generator - Data Template
 * 
 * Use this template to structure your research data for analysis and visualization.
 * All fields are required unless marked as optional.
 * 
 * Example usage:
 * ```typescript
 * import { IDEAS, MARKET_STATS, REFERENCES } from './research-template';
 * 
 * // Access ranked ideas
 * const topIdea = IDEAS[0];
 * console.log(topIdea.name, topIdea.score);
 * 
 * // Filter by category
 * const aiIdeas = IDEAS.filter(i => i.category === "AI Productivity");
 * 
 * // Calculate average score
 * const avgScore = IDEAS.reduce((sum, i) => sum + i.score, 0) / IDEAS.length;
 * ```
 */

// ─── Core Data Types ──────────────────────────────────────────────────────

export interface Idea {
  /** Ranking position (1-N) */
  rank: number;

  /** Unique identifier (kebab-case) */
  id: string;

  /** Idea name / product name */
  name: string;

  /** One-line tagline / value proposition */
  tagline: string;

  /** Composite opportunity score (1-10) */
  score: number;

  /** Category grouping (e.g., "AI Productivity", "Neurodivergent Tools") */
  category: string;

  /** Hex color code for visualization (#RRGGBB) */
  color: string;

  /** Market size (e.g., "$1.79B") */
  marketSize: string;

  /** Market size as number (USD billions) for calculations */
  marketSizeNum: number;

  /** Compound Annual Growth Rate (e.g., "11.9%") */
  cagr: string;

  /** Monthly subscription price (USD) */
  pricing: number;

  /** Number of paying users needed to hit revenue target */
  usersNeeded: number;

  /** Target MRR in USD */
  mrrUSD: number;

  /** Target MRR in local currency (e.g., AUD) */
  mrrAUD: number;

  /** Risk score (1-10, where 1 = low risk, 10 = very high risk) */
  risk: number;

  /** Founder-market fit scores across three dimensions (1-10 each) */
  founderFit: {
    ux: number;      // UX Designer skills alignment
    adhd: number;    // ADHD/neurodivergent lived experience
    dev: number;     // Indie developer capability
  };

  /** Weighted scores across evaluation criteria (1-10 each) */
  scores: {
    marketSize: number;      // 20% weight
    pmf: number;             // 30% weight (Product-Market Fit evidence)
    founderFit: number;       // 25% weight
    competitorGap: number;    // 15% weight
    revenueSpeed: number;     // 10% weight
  };

  /** 2-3 sentence problem statement */
  problem: string;

  /** Real user quotes validating the pain point */
  userQuotes: Array<{
    text: string;      // Direct quote
    source: string;    // Source (e.g., "u/username, r/subreddit")
    url: string;       // Clickable link for verification
  }>;

  /** Direct competitors and their weaknesses */
  competitors: Array<{
    name: string;      // Competitor name
    weakness: string;  // Why your idea is different
  }>;

  /** SWOT analysis */
  swot: {
    strengths: string[];      // Competitive advantages
    weaknesses: string[];     // Limitations and challenges
    opportunities: string[];  // Market tailwinds and expansion paths
    threats: string[];        // Risks and competitive threats
  };

  /** Revenue model description (e.g., "$7/month subscription") */
  revenueModel: string;

  /** Organic growth channels (e.g., "r/ADHD", "Product Hunt", "LinkedIn") */
  growthChannels: string[];

  /** Competitor gap scores per competitor (1-5 scale) */
  competitorGapScore: number[];
}

export interface MarketStat {
  /** Statistic label */
  label: string;

  /** Statistic value (e.g., "$7.8B", "3.45B", "22.5%") */
  value: string;

  /** Subtext / context (e.g., "2024 market size") */
  sub: string;

  /** Hex color for visualization */
  color: string;
}

export interface Reference {
  /** Reference number for citations */
  id: number;

  /** Full title of the source */
  title: string;

  /** Source name or publication */
  source: string;

  /** Direct URL to the source */
  url: string;
}

export interface RevenueProjection {
  /** Time period label (e.g., "Month 1", "Month 2") */
  month: string;

  /** Conservative scenario MRR */
  conservative: number;

  /** Realistic scenario MRR */
  realistic: number;

  /** Optimistic scenario MRR */
  optimistic: number;
}

export interface MarketGrowth {
  /** Year label */
  year: string;

  /** AI Extensions market size (USD billions) */
  aiExtensions: number;

  /** ADHD Apps market size (USD billions) */
  adhdApps: number;

  /** Accessibility Tools market size (USD billions) */
  accessibilityTools: number;
}

// ─── Sample Data ──────────────────────────────────────────────────────────

/**
 * Example: 10 validated Chrome extension micro-SaaS ideas
 * Replace with your own research data
 */
export const IDEAS: Idea[] = [
  {
    rank: 1,
    id: "adhd-tab-manager",
    name: "ADHD-Native Tab & Context Manager",
    tagline: "A tab manager that thinks like an ADHD brain",
    score: 9.2,
    category: "Neurodivergent Productivity",
    color: "#6366F1",
    marketSize: "$1.79B",
    marketSizeNum: 1.79,
    cagr: "11.9%",
    pricing: 7,
    usersNeeded: 286,
    mrrUSD: 2002,
    mrrAUD: 3100,
    risk: 2,
    founderFit: { ux: 8, adhd: 10, dev: 8 },
    scores: { marketSize: 9, pmf: 9, founderFit: 10, competitorGap: 9, revenueSpeed: 9 },
    problem: "ADHD users (15-20% of population) use browser tabs as external working memory, leading to thousands of open tabs, cognitive overload, and anxiety.",
    userQuotes: [
      {
        text: "My buddies were ripping on me because I had some 7,000-9,000 tabs open.",
        source: "u/bigblackglock17, r/ADHD",
        url: "https://www.reddit.com/r/ADHD/comments/1hqu6oe/"
      }
    ],
    competitors: [
      { name: "OneTab", weakness: "Saves tabs but no ADHD-specific UX" },
      { name: "Toby", weakness: "Beautiful but complex, not neurodivergent-optimized" }
    ],
    swot: {
      strengths: ["Founder lived experience", "Large underserved market", "Clear differentiation"],
      weaknesses: ["Behavior change required", "Inconsistent payment habits"],
      opportunities: ["Rising ADHD diagnosis rates", "Neurodivergent workplace inclusion"],
      threats: ["Big players adding features", "Free alternatives emerging"]
    },
    revenueModel: "$7/month or $49/year subscription",
    growthChannels: ["r/ADHD", "r/productivity", "ADHD Twitter/X", "Product Hunt"],
    competitorGapScore: [5, 4, 3, 5, 5]
  }
  // Add more ideas here...
];

/**
 * Market context statistics
 */
export const MARKET_STATS: MarketStat[] = [
  {
    label: "Browser Extension Market",
    value: "$7.8B",
    sub: "2024 market size",
    color: "#6366F1"
  },
  {
    label: "Chrome Users Globally",
    value: "3.45B",
    sub: "67.7% browser share",
    color: "#10B981"
  }
  // Add more stats...
];

/**
 * 6-month revenue projection scenarios
 */
export const REVENUE_PROJECTION_DATA: RevenueProjection[] = [
  { month: "Launch", conservative: 0, realistic: 0, optimistic: 0 },
  { month: "Month 1", conservative: 150, realistic: 300, optimistic: 600 },
  { month: "Month 2", conservative: 450, realistic: 700, optimistic: 1200 },
  { month: "Month 3", conservative: 900, realistic: 1400, optimistic: 2200 }
  // Add more months...
];

/**
 * Market growth trends (2024-2030)
 */
export const MARKET_GROWTH_DATA: MarketGrowth[] = [
  { year: "2024", aiExtensions: 1.2, adhdApps: 1.21, accessibilityTools: 1.2 },
  { year: "2025", aiExtensions: 1.47, adhdApps: 1.79, accessibilityTools: 1.30 }
  // Add more years...
];

/**
 * Category to color mapping
 */
export const CATEGORY_COLORS: Record<string, string> = {
  "Neurodivergent Productivity": "#6366F1",
  "AI Productivity": "#F43F5E",
  "UX Design Tools": "#10B981",
  "Freelancer Productivity": "#F59E0B"
};

/**
 * All cited sources and references
 */
export const REFERENCES: Reference[] = [
  {
    id: 1,
    title: "Chrome Extensions Market Latest Growth & Impact Analysis",
    source: "HTF Market Intelligence",
    url: "https://www.openpr.com/news/3785082/chrome-extensions-market-latest-growth-impact-analysis"
  },
  {
    id: 2,
    title: "AI-powered Chrome Extension Market Size | CAGR of 22.5%",
    source: "Market.us",
    url: "https://market.us/report/ai-powered-chrome-extension-market/"
  }
  // Add more references...
];

// ─── Helper Functions ──────────────────────────────────────────────────────

/**
 * Calculate composite opportunity score from weighted criteria
 */
export function calculateCompositeScore(idea: Idea): number {
  const weights = {
    marketSize: 0.20,
    pmf: 0.30,
    founderFit: 0.25,
    competitorGap: 0.15,
    revenueSpeed: 0.10
  };

  return (
    idea.scores.marketSize * weights.marketSize +
    idea.scores.pmf * weights.pmf +
    idea.scores.founderFit * weights.founderFit +
    idea.scores.competitorGap * weights.competitorGap +
    idea.scores.revenueSpeed * weights.revenueSpeed
  );
}

/**
 * Sort ideas by score (highest first)
 */
export function sortByScore(ideas: Idea[]): Idea[] {
  return [...ideas].sort((a, b) => b.score - a.score);
}

/**
 * Filter ideas by category
 */
export function filterByCategory(ideas: Idea[], category: string): Idea[] {
  if (category === "All") return ideas;
  return ideas.filter(idea => idea.category === category);
}

/**
 * Get top N ideas
 */
export function getTopIdeas(ideas: Idea[], n: number = 3): Idea[] {
  return sortByScore(ideas).slice(0, n);
}

/**
 * Calculate average score across all ideas
 */
export function getAverageScore(ideas: Idea[]): number {
  if (ideas.length === 0) return 0;
  return ideas.reduce((sum, idea) => sum + idea.score, 0) / ideas.length;
}

/**
 * Get ideas by risk level
 */
export function getIdeasByRisk(ideas: Idea[], maxRisk: number): Idea[] {
  return ideas.filter(idea => idea.risk <= maxRisk);
}

/**
 * Calculate users needed for a given MRR target
 */
export function calculateUsersNeeded(
  targetMRR: number,
  monthlyPrice: number,
  conversionRate: number = 0.01
): number {
  return Math.ceil(targetMRR / (monthlyPrice * conversionRate));
}

/**
 * Format currency for display
 */
export function formatCurrency(value: number, currency: string = "USD"): string {
  const formatter = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: currency === "AUD" ? "AUD" : "USD",
    minimumFractionDigits: 0
  });
  return formatter.format(value);
}
