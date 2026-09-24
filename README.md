# CUSTOMER SENTIMENT ANALYTICS
### *Analyzing Customer Reviews, Sentiments & Emotions using NLP*

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://www.python.org/)
[![NLTK VADER](https://img.shields.io/badge/NLP-NLTK%20VADER-purple)](https://www.nltk.org/)
[![License](https://img.shields.io/badge/License-Academic%20%2F%20Open-lightgrey)]()
[![Design Identity](https://img.shields.io/badge/Theme-White%20%2B%20Purple-7B2CBF)]()
[![Creator](https://img.shields.io/badge/Creator-Harshita%20Tomer-3B1E54)]()

---

## 📌 Executive Overview

**CUSTOMER SENTIMENT ANALYTICS** is an end-to-end Data Analytics and Natural Language Processing (NLP) capstone project engineered to analyze authentic consumer feedback from the **Amazon Alexa Ecosystem**. 

Rather than treating customer reviews merely as numerical 1-to-5 star ratings, this project unpacks the granular voice of the customer. By combining **NLTK VADER** (Valence Aware Dictionary and sEntiment Reasoner) with an explainable, psychologically-grounded **Emotion Lexicon**, the project extracts sentiment polarity, discrete customer emotions, key product praise points, and critical operational bottlenecks across 16 hardware variations.

The entire project follows a cohesive **White + Purple + Light Lavender** visual identity across 12 publication-ready visualizations, interactive KPI cards, and an academic project report.

---

## 🎯 Problem Statement

In modern consumer electronics and e-commerce:
1. **Rating Discrepancies**: Star ratings alone often mask critical flaws; consumers frequently assign 4 stars while reporting critical software disconnects or setup failures.
2. **High-Volume Feedback**: Product teams cannot manually review thousands of monthly submissions, causing delayed responses to firmware regressions.
3. **Absence of Emotional Granularity**: Standard polarity classifiers (positive vs. negative) fail to differentiate between **Anger** (indignation regarding broken hardware) and **Sadness** (disappointment with sound quality).
4. **Siloed Product Variations**: Cross-model performance comparison (e.g. Echo Dot vs. Echo Show vs. Fire TV Stick) is rarely synthesized into unified comparative intelligence.

---

## 🚀 Key Project Objectives

* **Data Engineering**: Ingest, deduplicate, and normalize 3,150 authentic Amazon customer reviews.
* **Exploratory Data Analysis**: Profile star rating distributions, review word lengths, product variations, and submission date trends.
* **Sentiment Classification**: Apply VADER to quantify continuous compound polarity (-1.0 to +1.0) and partition reviews into Positive, Neutral, and Negative classes.
* **Discrete Emotion Mining**: Map customer vocabulary to six emotional states: *Joy, Neutral/Other, Fear, Sadness, Anger, and Surprise*.
* **Keyword Discovery**: Uncover top praise and complaint terms and render stylized White + Purple Word Clouds.
* **Hardware Benchmarking**: Benchmark satisfaction rates across 16 product variations.
* **Strategic Business Support**: Formulate empirical, non-fabricated recommendations for product managers, firmware engineers, and customer support leads.

---

## 📊 Dataset Provenance & Description

* **Source**: Publicly available **Amazon Alexa Customer Reviews Dataset** (widely used in academic machine learning and NLP benchmarks).
* **Format**: Tab-Separated Values (`.tsv`)
* **Raw Record Count**: 3,150 customer reviews
* **Cleaned Record Count**: 2,435 unique verified customer reviews (715 duplicates removed)
* **Attributes**:
  * `rating`: Discrete star rating from 1 to 5
  * `date`: Submission timestamp (May 2018 – July 2018)
  * `variation`: Hardware model or finish (e.g., Charcoal Fabric, Heather Gray Fabric, Echo Dot, Echo Show, Fire TV Stick)
  * `verified_reviews`: Unstructured text containing customer opinions
  * `feedback`: Binary satisfaction ground truth (1 = positive, 0 = negative)

*Note: The project uses 100% authentic, real-world customer reviews. No synthetic or generated data is introduced.*

---

## 🛠️ Technology Stack

| Layer | Library / Tool | Primary Function |
| :--- | :--- | :--- |
| **Language** | Python 3.12 | Core programming runtime |
| **Data Manipulation** | Pandas & NumPy | Tabular transformation, deduplication, vectorized scoring |
| **Natural Language Processing** | NLTK (VADER) | Rule-based sentiment valence scoring, negation handling |
| **Emotion Mining** | Custom Emotion Lexicon | Plutchik & Ekman grounded discrete emotion classification |
| **Data Visualization** | Matplotlib & Seaborn | 12 custom White + Purple publication-ready charts |
| **Lexical Clouds** | WordCloud | High-resolution purple/lavender word frequency visualizations |
| **Report Generation** | Python-docx | Programmatic synthesis of 24-section formal project report |
| **Execution Engine** | Jupyter / nbclient | Programmatic cell execution with embedded outputs |

---

## 📁 Submission Directory Structure

```text
Customer_Sentiment_Analytics/
│
├── Customer_Sentiment_Analytics.ipynb           # Complete, executed Jupyter Notebook with outputs
├── requirements.txt                             # Lean, verified Python dependencies
├── Customer_Sentiment_Analytics_Project_Report.docx # Professional 24-section Word project report
├── README.md                                    # Comprehensive project documentation
│
├── amazon_alexa.tsv                             # Real Amazon customer review dataset
└── figures/                                     # 12 White + Purple dashboard visualizations
    ├── 01_rating_distribution.png
    ├── 02_sentiment_distribution.png
    ├── 03_emotion_distribution.png
    ├── 04_sentiment_vs_rating.png
    ├── 05_category_wise_sentiment.png
    ├── 06_positive_vs_negative.png
    ├── 07_review_length_distribution.png
    ├── 08_monthly_sentiment_trend.png
    ├── 09_top_positive_keywords.png
    ├── 10_top_negative_keywords.png
    ├── 11_positive_wordcloud.png
    └── 12_negative_wordcloud.png
```

---

## ⚙️ Installation & Setup Instructions

### 1. Clone or Navigate to the Project Directory
```bash
cd "Customer_Sentiment_Analytics"
```

### 2. Create and Activate a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download Required NLTK Corpora (Automated inside notebook, or manual):
```python
import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
```

---

## 🏃 How to Run the Project

### Option A: Launching via Jupyter Notebook / JupyterLab
```bash
jupyter notebook Customer_Sentiment_Analytics.ipynb
```
Select **Kernel -> Restart & Run All** to re-execute the entire pipeline from scratch.

### Option B: Viewing in VS Code
Open the repository in VS Code, click on `Customer_Sentiment_Analytics.ipynb`, select your Python kernel, and execute cells interactively.

---

## 🔬 Methodology & Analytics Workflow

```text
  [ Raw Amazon Customer Reviews ] (3,150 Records)
                 ↓
  [ Data Cleaning & Normalization ]
     • Deduplication (-715 rows → 2,435 unique)
     • Null imputation & regex cleanup
     • Feature engineering (word_count, char_length, dates)
                 ↓
  [ Exploratory Data Analysis ]
     • Star ratings (1-5 stars)
     • Review word count distributions (mean = 19.5 words)
     • Hardware variation popularity & monthly trends
                 ↓
  [ Sentiment Analysis (NLTK VADER) ]
     • Compound Polarity Score (-1.0 to +1.0)
     • Positive: 81.52% | Neutral: 11.13% | Negative: 7.35%
                 ↓
  [ Emotion Mining (Lexicon Framework) ]
     • Joy: 62.40% | Neutral: 32.33% | Fear: 2.01%
     • Sadness: 1.77% | Anger: 1.44% | Surprise: 0.04%
                 ↓
  [ Keyword & Lexical Discovery ]
     • Top positive: love (736), great (555), music (328)
     • Top negative: alarm (30), screen (28), connect (16)
     • Color-themed Word Clouds
                 ↓
  [ Executive Dashboard & Business Recommendations ]
     • Hardware audio & acoustic upgrades
     • Firmware WiFi self-healing reconnection
     • Conversational voice tolerance
     • Multilingual Spanish expansion
```

---

## 📈 Key Empirical Findings

1. **High Baseline Satisfaction**: 
   * Average star rating is **4.44 / 5.00**.
   * Over **81.52%** of reviews express positive sentiment.
2. **Aesthetic Material Premium**:
   * Fabric-finished models—**Charcoal Fabric** (89.04% positive, 3.20% negative) and **Heather Gray Fabric** (88.61% positive, 2.53% negative)—consistently outscore standard plastic finishes (**Black** at 11.88% negative, **White** at 10.00% negative).
3. **Review Length as Dissatisfaction Proxy**:
   * Satisfied reviews are short and enthusiastic (mean word count: **20.1 words**).
   * Critical negative reviews average **38.6 words**—nearly double the length—serving as diagnostic post-mortems of specific defects.
4. **Dominant Emotional States**:
   * **Joy (62.40%)** is the primary emotion driver.
   * Negative emotions are split between **Fear (2.01%)** (privacy, dropped connections), **Sadness (1.77%)** (disappointment with sound), and **Anger (1.44%)** (glitches and frustration).

---

## 💡 Actionable Business Recommendations

* **Acoustics & Audio Differentiation**: Customers expect clear generational improvements. Focus engineering on bass response for mid-tier models (Echo Dot) and market acoustic upgrades prominently.
* **Firmware Self-Healing Reconnect**: Smart plug and smart lighting disconnections account for substantial 1-star reviews. Implement background reconnect protocols that recover lost connections without requiring manual factory resets.
* **Voice Phrasing Flexibility**: Reduce conversational rigidity in the NLU engine so users do not experience cognitive friction trying to phrase commands for basic tasks.
* **Multilingual Localization**: Accelerate bilingual English/Spanish voice recognition to serve a highly enthusiastic international customer base.

---

## ⚠️ Limitations & Future Scope

### Limitations
* **Lexicon Boundaries**: VADER and rule-based emotion lexicons rely on predefined lexical dictionaries; nuanced irony, extreme sarcasm, or novel internet slang may be classified as Neutral.
* **Sample Class Imbalance**: As typical with consumer electronics, 81.5% of reviews are positive, yielding a focused sample (179 reviews) of negative feedback.

### Future Scope
* **Aspect-Based Sentiment Analysis (ABSA)**: Deconstruct reviews into sentence clauses to score individual product dimensions (e.g. *Sound Quality: +0.9*, *WiFi Reliability: -0.6*).
* **Real-Time Streaming Pipelines**: Ingest streaming e-commerce reviews to trigger real-time anomaly alerts for firmware regressions within 24 hours of release.

---

## 📜 Academic Integrity & Citation

This project was developed strictly adhering to academic integrity standards. All statistics and figures are computed directly from the designated Amazon customer review dataset.

```bibtex
@article{vader2014,
  title={VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text},
  author={Hutto, C. J. and Gilbert, E.},
  journal={Proceedings of the International AAAI Conference on Web and Social Media},
  year={2014}
}
```
---

<div align="center">
  <p style="color: #3B1E54; font-weight: 600; font-size: 13px; margin: 0;">Created by Harshita Tomer</p>
  <p style="color: #7B2CBF; font-size: 11px; margin-top: 4px;">CUSTOMER SENTIMENT ANALYTICS • White + Purple Dashboard Edition</p>
</div>
