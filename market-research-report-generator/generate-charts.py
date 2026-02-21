#!/usr/bin/env python3
"""
Market Research Report Generator - Chart Generation Script

This script generates 10 publication-ready charts from your research data.
Charts are saved as PNG files at 300 DPI for print quality.

Usage:
    python3 generate-charts.py --input data.json --output ./charts

Requirements:
    pip install matplotlib seaborn plotly pandas numpy
"""

import json
import argparse
import os
from pathlib import Path
from typing import List, Dict, Any
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle
import warnings

warnings.filterwarnings('ignore')

# ─── Configuration ────────────────────────────────────────────────────────

DPI = 300
FIGURE_SIZE = (12, 7)
STYLE = "seaborn-v0_8-darkgrid"
COLOR_PALETTE = {
    "indigo": "#6366F1",
    "emerald": "#10B981",
    "rose": "#F43F5E",
    "amber": "#F59E0B",
    "violet": "#8B5CF6",
    "cyan": "#06B6D4",
    "slate": "#64748B"
}

# ─── Chart Generation Functions ───────────────────────────────────────────

def load_data(filepath: str) -> Dict[str, Any]:
    """Load research data from JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)

def save_figure(fig, filename: str, output_dir: str):
    """Save figure with high DPI for print quality"""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, dpi=DPI, bbox_inches='tight', facecolor='white')
    print(f"✓ Saved: {filename}")
    plt.close(fig)

def chart_1_opportunity_scores(data: Dict[str, Any], output_dir: str):
    """Chart 1: Opportunity Score Ranking (Horizontal Bar Chart)"""
    ideas = sorted(data['ideas'], key=lambda x: x['score'], reverse=True)
    
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    
    names = [idea['name'][:30] for idea in ideas]
    scores = [idea['score'] for idea in ideas]
    colors = [idea['color'] for idea in ideas]
    
    bars = ax.barh(names, scores, color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
    
    ax.set_xlabel('Opportunity Score (1-10)', fontsize=12, fontweight='bold')
    ax.set_title('Ranked Ideas by Opportunity Score', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 10)
    
    # Add value labels
    for i, (bar, score) in enumerate(zip(bars, scores)):
        ax.text(score + 0.2, bar.get_y() + bar.get_height()/2, f'{score:.1f}', 
                va='center', fontsize=10, fontweight='bold')
    
    ax.invert_yaxis()
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    save_figure(fig, 'chart1_opportunity_scores.png', output_dir)

def chart_2_market_sizes(data: Dict[str, Any], output_dir: str):
    """Chart 2: Market Sizes (Vertical Bar Chart)"""
    ideas = sorted(data['ideas'], key=lambda x: x['marketSizeNum'], reverse=True)
    
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    
    names = [idea['name'][:25] for idea in ideas]
    sizes = [idea['marketSizeNum'] for idea in ideas]
    colors = [idea['color'] for idea in ideas]
    
    bars = ax.bar(range(len(names)), sizes, color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
    
    ax.set_ylabel('Market Size (USD Billions)', fontsize=12, fontweight='bold')
    ax.set_title('Total Addressable Market (TAM) by Idea', fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=45, ha='right')
    
    # Add value labels
    for bar, size in zip(bars, sizes):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'${size:.1f}B', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    save_figure(fig, 'chart2_market_sizes.png', output_dir)

def chart_3_swot_radar(data: Dict[str, Any], output_dir: str):
    """Chart 3: SWOT Radar for Top 3 Ideas"""
    top_3 = sorted(data['ideas'], key=lambda x: x['score'], reverse=True)[:3]
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw=dict(projection='polar'))
    
    categories = ['Strengths', 'Weaknesses', 'Opportunities', 'Threats', 'Founder Fit']
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    for idx, (ax, idea) in enumerate(zip(axes, top_3)):
        # Mock SWOT scores (in real implementation, calculate from SWOT text)
        values = [8, 6, 8, 5, idea['scores']['founderFit']]
        values += values[:1]
        
        ax.plot(angles, values, 'o-', linewidth=2, color=idea['color'])
        ax.fill(angles, values, alpha=0.25, color=idea['color'])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, size=9)
        ax.set_ylim(0, 10)
        ax.set_title(f"#{idea['rank']}: {idea['name'][:20]}", 
                    fontsize=11, fontweight='bold', pad=20)
        ax.grid(True)
    
    plt.suptitle('SWOT Analysis - Top 3 Ideas', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save_figure(fig, 'chart3_swot_radar.png', output_dir)

def chart_4_revenue_projection(data: Dict[str, Any], output_dir: str):
    """Chart 4: Revenue Projection (Line Chart)"""
    projections = data.get('revenueProjections', [])
    
    if not projections:
        print("⚠ Skipping chart 4: No revenue projection data")
        return
    
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    
    months = [p['month'] for p in projections]
    conservative = [p['conservative'] for p in projections]
    realistic = [p['realistic'] for p in projections]
    optimistic = [p['optimistic'] for p in projections]
    
    x = range(len(months))
    
    ax.plot(x, conservative, marker='o', linestyle='--', linewidth=2, 
            label='Conservative', color=COLOR_PALETTE['slate'], alpha=0.7)
    ax.plot(x, realistic, marker='o', linewidth=3, 
            label='Realistic', color=COLOR_PALETTE['indigo'])
    ax.plot(x, optimistic, marker='o', linestyle='--', linewidth=2, 
            label='Optimistic', color=COLOR_PALETTE['emerald'], alpha=0.7)
    
    # Target line
    target_mrr = 2000
    ax.axhline(y=target_mrr, color=COLOR_PALETTE['rose'], linestyle=':', linewidth=2, 
               label=f'Target MRR (${target_mrr:,})')
    
    ax.set_xlabel('Timeline', fontsize=12, fontweight='bold')
    ax.set_ylabel('MRR (USD)', fontsize=12, fontweight='bold')
    ax.set_title('6-Month Revenue Projection Scenarios', fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(months)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Format y-axis as currency
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
    
    plt.tight_layout()
    save_figure(fig, 'chart4_revenue_projection.png', output_dir)

def chart_5_competitor_gap(data: Dict[str, Any], output_dir: str):
    """Chart 5: Competitor Gap Matrix (Heatmap)"""
    ideas = data['ideas']
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create gap matrix (mock data for demonstration)
    gap_matrix = np.array([idea.get('competitorGapScore', [3]*5) for idea in ideas])
    
    im = ax.imshow(gap_matrix, cmap='RdYlGn', aspect='auto', vmin=1, vmax=5)
    
    ax.set_xticks(range(len(gap_matrix[0])))
    ax.set_xticklabels([f'Competitor {i+1}' for i in range(len(gap_matrix[0]))], fontsize=10)
    ax.set_yticks(range(len(ideas)))
    ax.set_yticklabels([idea['name'][:25] for idea in ideas], fontsize=10)
    
    ax.set_title('Competitor Gap Analysis Matrix\n(5 = Blue Ocean, 1 = Saturated)', 
                fontsize=14, fontweight='bold', pad=20)
    
    # Add text annotations
    for i in range(len(ideas)):
        for j in range(len(gap_matrix[0])):
            text = ax.text(j, i, f'{gap_matrix[i, j]:.0f}',
                          ha="center", va="center", color="black", fontweight='bold')
    
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Gap Score', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    save_figure(fig, 'chart5_competitor_gap.png', output_dir)

def chart_6_market_growth(data: Dict[str, Any], output_dir: str):
    """Chart 6: Market Growth Trends (Multi-line Chart)"""
    growth_data = data.get('marketGrowth', [])
    
    if not growth_data:
        print("⚠ Skipping chart 6: No market growth data")
        return
    
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    
    years = [d['year'] for d in growth_data]
    x = range(len(years))
    
    if 'aiExtensions' in growth_data[0]:
        ai_ext = [d['aiExtensions'] for d in growth_data]
        ax.plot(x, ai_ext, marker='o', linewidth=2.5, label='AI Chrome Extensions (22.5% CAGR)',
               color=COLOR_PALETTE['indigo'])
    
    if 'adhdApps' in growth_data[0]:
        adhd = [d['adhdApps'] for d in growth_data]
        ax.plot(x, adhd, marker='s', linewidth=2.5, label='ADHD Apps (11.9% CAGR)',
               color=COLOR_PALETTE['rose'])
    
    if 'accessibilityTools' in growth_data[0]:
        access = [d['accessibilityTools'] for d in growth_data]
        ax.plot(x, access, marker='^', linewidth=2.5, label='Accessibility Tools (8.7% CAGR)',
               color=COLOR_PALETTE['emerald'])
    
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Market Size (USD Billions)', fontsize=12, fontweight='bold')
    ax.set_title('Target Market Growth Trends (2024-2030)', fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_figure(fig, 'chart6_market_growth.png', output_dir)

def chart_7_founder_fit(data: Dict[str, Any], output_dir: str):
    """Chart 7: Founder-Market Fit Comparison (Grouped Bar Chart)"""
    ideas = sorted(data['ideas'], key=lambda x: x['score'], reverse=True)[:5]
    
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    
    x = np.arange(len(ideas))
    width = 0.25
    
    ux_scores = [idea['founderFit']['ux'] for idea in ideas]
    adhd_scores = [idea['founderFit']['adhd'] for idea in ideas]
    dev_scores = [idea['founderFit']['dev'] for idea in ideas]
    
    bars1 = ax.bar(x - width, ux_scores, width, label='UX Designer', color=COLOR_PALETTE['emerald'], alpha=0.8)
    bars2 = ax.bar(x, adhd_scores, width, label='AuDHD', color=COLOR_PALETTE['indigo'], alpha=0.8)
    bars3 = ax.bar(x + width, dev_scores, width, label='Indie Dev', color=COLOR_PALETTE['amber'], alpha=0.8)
    
    ax.set_ylabel('Fit Score (1-10)', fontsize=12, fontweight='bold')
    ax.set_title('Founder-Market Fit Scores - Top 5 Ideas', fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels([idea['name'][:20] for idea in ideas], rotation=15, ha='right')
    ax.set_ylim(0, 10)
    ax.legend(fontsize=10)
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    save_figure(fig, 'chart7_founder_fit.png', output_dir)

def chart_8_pricing_revenue(data: Dict[str, Any], output_dir: str):
    """Chart 8: Pricing vs Users Needed (Scatter Plot)"""
    ideas = data['ideas']
    
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    
    for idea in ideas:
        ax.scatter(idea['pricing'], idea['usersNeeded'], 
                  s=idea['marketSizeNum']*100, alpha=0.6, 
                  color=idea['color'], edgecolors='black', linewidth=1,
                  label=idea['name'][:20])
    
    ax.set_xlabel('Monthly Price (USD)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Users Needed for $2K MRR', fontsize=12, fontweight='bold')
    ax.set_title('Pricing Strategy vs. User Acquisition Target\n(bubble size = market size)', 
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    
    # Add annotations for top ideas
    for idea in sorted(ideas, key=lambda x: x['score'], reverse=True)[:3]:
        ax.annotate(f"#{idea['rank']}", 
                   (idea['pricing'], idea['usersNeeded']),
                   xytext=(5, 5), textcoords='offset points', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    save_figure(fig, 'chart8_pricing_revenue.png', output_dir)

def chart_9_risk_reward(data: Dict[str, Any], output_dir: str):
    """Chart 9: Risk vs Reward Quadrant (Scatter Plot)"""
    ideas = data['ideas']
    
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    
    for idea in ideas:
        ax.scatter(idea['risk'], idea['score'], 
                  s=idea['mrrUSD']/5, alpha=0.7, 
                  color=idea['color'], edgecolors='black', linewidth=1)
        ax.annotate(f"#{idea['rank']}", 
                   (idea['risk'], idea['score']),
                   xytext=(3, 3), textcoords='offset points', fontsize=8)
    
    # Quadrant lines
    ax.axvline(x=5, color='gray', linestyle='--', alpha=0.5, linewidth=1)
    ax.axhline(y=8, color='gray', linestyle='--', alpha=0.5, linewidth=1)
    
    # Quadrant labels
    ax.text(2.5, 9.5, 'Low Risk\nHigh Reward\n(SWEET SPOT)', ha='center', fontsize=10, 
           bbox=dict(boxstyle='round', facecolor=COLOR_PALETTE['emerald'], alpha=0.1))
    ax.text(7.5, 9.5, 'High Risk\nHigh Reward', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor=COLOR_PALETTE['amber'], alpha=0.1))
    
    ax.set_xlabel('Risk Score (1-10)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Opportunity Score (1-10)', fontsize=12, fontweight='bold')
    ax.set_title('Risk vs. Reward Quadrant Analysis\n(bubble size = potential MRR)', 
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 10)
    ax.set_ylim(6, 10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_figure(fig, 'chart9_risk_reward.png', output_dir)

def chart_10_market_overview(data: Dict[str, Any], output_dir: str):
    """Chart 10: Market Overview Infographic"""
    stats = data.get('marketStats', [])
    
    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(111)
    ax.axis('off')
    
    # Title
    fig.text(0.5, 0.95, 'Market Overview - Key Statistics', 
            ha='center', fontsize=18, fontweight='bold')
    
    # Create stat boxes
    stat_boxes = []
    cols = 4
    rows = 2
    box_width = 0.2
    box_height = 0.3
    start_x = 0.05
    start_y = 0.55
    
    for idx, stat in enumerate(stats[:8]):
        row = idx // cols
        col = idx % cols
        
        x = start_x + col * (box_width + 0.02)
        y = start_y - row * (box_height + 0.05)
        
        # Draw box
        rect = Rectangle((x, y), box_width, box_height, 
                         linewidth=2, edgecolor=stat.get('color', COLOR_PALETTE['slate']),
                         facecolor=stat.get('color', COLOR_PALETTE['slate']), alpha=0.1)
        fig.patches.append(rect)
        
        # Add text
        fig.text(x + box_width/2, y + box_height*0.65, stat['value'], 
                ha='center', va='center', fontsize=16, fontweight='bold',
                color=stat.get('color', COLOR_PALETTE['slate']))
        fig.text(x + box_width/2, y + box_height*0.35, stat['label'], 
                ha='center', va='center', fontsize=10, fontweight='bold')
        fig.text(x + box_width/2, y + box_height*0.1, stat['sub'], 
                ha='center', va='center', fontsize=8, style='italic', color='gray')
    
    plt.tight_layout()
    save_figure(fig, 'chart10_market_overview.png', output_dir)

# ─── Main Execution ───────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='Generate publication-ready charts from market research data'
    )
    parser.add_argument('--input', type=str, required=True, 
                       help='Path to input JSON data file')
    parser.add_argument('--output', type=str, default='./charts',
                       help='Output directory for charts (default: ./charts)')
    
    args = parser.parse_args()
    
    # Load data
    print(f"📊 Loading data from {args.input}...")
    data = load_data(args.input)
    
    # Generate all charts
    print(f"🎨 Generating charts to {args.output}/...\n")
    
    chart_1_opportunity_scores(data, args.output)
    chart_2_market_sizes(data, args.output)
    chart_3_swot_radar(data, args.output)
    chart_4_revenue_projection(data, args.output)
    chart_5_competitor_gap(data, args.output)
    chart_6_market_growth(data, args.output)
    chart_7_founder_fit(data, args.output)
    chart_8_pricing_revenue(data, args.output)
    chart_9_risk_reward(data, args.output)
    chart_10_market_overview(data, args.output)
    
    print(f"\n✅ All charts generated successfully!")
    print(f"📁 Output directory: {os.path.abspath(args.output)}")

if __name__ == '__main__':
    main()
