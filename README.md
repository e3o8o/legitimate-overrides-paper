# Legitimate Overrides in Decentralized Protocols

**Paper repository for Elem Oghenekaro & Nimrod Talmon - "Legitimate Overrides in Decentralized Protocols"**  
*Focus: Emergency governance mechanisms and legitimacy trade-offs in decentralized systems*

> "That which is measured improves. That which is measured and reported improves exponentially."

---

## Datasets Overview

### Core Research Data
- 705 total exploits documented (2016-2026)
- 605 intervention-eligible technical exploits ($10.21B addressable)
- 130 actual interventions with emergency mechanism activations
- 52 curated metrics cases with verified timing and outcomes

### Key Findings
- **Power Law Distribution**: Losses follow fat-tailed distribution (α=1.32)
- **Speed-Scope-Success Paradox**: Trade-offs between response speed, scope, and effectiveness
- **Authority Performance**: Signer Set (fast, frequent), Delegated Body (balanced), Governance (deliberate but high success for network scope)

## Analysis Pipeline

### Complete Analysis Notebook
The `notebooks/paper_analysis_complete.ipynb` provides end-to-end analysis:

1. **Data Loading & Stratification**
   - Loads all datasets and creates intervention-eligible universe
   - Separates systemic failures from technical exploits

2. **Sentiment Analysis Pipeline**
   - Forum sentiment analysis (Discourse API integration)
   - Twitter sentiment analysis (API v2)
   - Combined sentiment scoring using VADER
   - 271 total posts analyzed across 10 intervention cases

3. **Intervention Mechanism Calculator**
   - Stochastic cost model: `ExpectedCost = Centralization + P × (Time×Damage + BlastRate)`
   - Scenario analysis for different urgency levels
   - Political analogy mapping (Oligarchy, Representative Democracy, Direct Democracy)

4. **Figure Generation** (8 figures)
   - Pareto loss distribution (lof01)
   - Four-layer timeline (lof02) 
   - Top 10 exploits (lof03)
   - Attack vector distribution (lof04)
   - Intervention effectiveness (lof05)
   - Authority distribution (lof06)
   - Scope-Authority matrix (lof07)
   - Containment time analysis (lof08)

5. **Statistical Analysis**
   - Power law fitting with Kolmogorov-Smirnov test
   - Authority performance metrics
   - Speed-Scope-Success Paradox analysis (filtered for data quality)

### Environment Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run complete analysis pipeline
jupyter lab notebooks/paper_analysis_complete.ipynb
```

### Paper Compilation

The paper can be compiled in two modes: **Full** (complete appendices) and **Concise** (12-page body for D2 conference submission).

#### 1. Full Version (38 pages)
Contains all content, including full appendices and raw tables.
```bash
cd paper/
pdflatex main.tex        # compile source
bibtex main              # process bibliography
pdflatex main.tex        # resolve citations
pdflatex main.tex        # finalize cross-references
# Output: main.pdf
```

#### 2. Concise Version (21 pages)
Optimized for D2 conference submission. Body limited to 12 pages; supplementary figures and detailed analysis moved to appendix.
```bash
cd paper/
pdflatex main_concise.tex  # compile wrapper (sets \concisetrue)
bibtex main_concise        # process bibliography
pdflatex main_concise.tex  # resolve citations
pdflatex main_concise.tex  # finalize cross-references
# Output: main_concise.pdf
```

## Research Contributions

1. Typology Development: 5×3 framework for emergency interventions
2. Empirical Analysis: First large-scale study of intervention effectiveness
3. Cost-Benefit Model: Quantitative framework for mechanism selection
4. Political Theory Bridge: Connecting blockchain governance to constitutional theory
5. Design Implications: Evidence-based recommendations for protocol architects

---

## License

CC-BY 4.0.
