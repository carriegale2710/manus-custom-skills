# Manus Custom Skills Repository

This repository serves as a backup and version control system for custom skills created in Manus AI.

## 📂 Skills Included

### 1. market-research-report-generator
A comprehensive skill for generating data-driven market research reports with SWOT analysis, competitor gap analysis, PDF documentation, and interactive web dashboards.

**Features:**
- 6-phase workflow for market research
- Weighted scoring system (5 criteria)
- 10 publication-ready charts
- Professional PDF reports
- Interactive React dashboards
- Real user validation from social media

**Use Cases:**
- Validate 5-15 business ideas before building
- Rank opportunities by weighted criteria
- Create investor pitch decks
- Competitive analysis and market sizing
- Product strategy and roadmapping

**Quick Start:** See `market-research-report-generator/QUICKSTART.md`

**Full Documentation:** See `market-research-report-generator/SKILL.md`

---

## 🚀 How to Use These Skills

1. Clone this repository
2. Copy any skill folder to `/home/ubuntu/skills/` in your Manus AI environment
3. Read the skill's `QUICKSTART.md` for quick start instructions
4. Read the skill's `SKILL.md` for comprehensive documentation

## 📝 Adding New Skills

To add a new skill to this repo:

1. Create the skill in Manus AI following the skill-creator guidelines
2. Copy the skill folder to this repo
3. Commit and push to GitHub

```bash
cp -r /home/ubuntu/skills/your-new-skill ./
git add your-new-skill/
git commit -m "Add: your-new-skill"
git push
```

## 📋 Skill Structure

Each skill should include:
- `SKILL.md` - Comprehensive documentation
- `QUICKSTART.md` - Quick start guide
- `README.md` - Overview and FAQ
- `skill.json` - Metadata
- Supporting templates, scripts, or components

## 🔄 Version Control

This repo uses Git for version control. Each skill can be updated independently:

```bash
git log --oneline  # View history
git diff           # See changes
git checkout <commit>  # Revert to previous version
```

## 📞 Support

For questions about a specific skill, refer to its documentation:
- Quick questions → `QUICKSTART.md`
- Detailed questions → `SKILL.md`
- General info → `README.md`

---

**Created:** February 2026  
**Purpose:** Backup and version control for custom Manus AI skills
