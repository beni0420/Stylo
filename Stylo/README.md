

  <div>
    <a href="README.es.md">🇪🇸 Español</a> | <strong>🇬🇧 English</strong>
  </div>

# Stylo – AI-Powered Multilingual Linguistic & Stylometric Analyzer

**Stylo** is a responsive, intelligent web application designed for real-time stylometric and linguistic analysis. Built using **Flask**, **spaCy**, and **Chart.js**, it leverages advanced Natural Language Processing (NLP) pipelines to evaluate text metrics, lexical diversity, syntactic structure, and automated language verification across multiple languages (**English, Spanish, French, and Italian**).

---

##  Key Features

* **AI & NLP Pipeline Integration**: Powered by `spaCy` tokenization, part-of-speech (POS) tagging, and sentence boundary detection to dissect text semantics and syntax.
* **Automated Language Guardrails**: Uses `langdetect` to verify that the inputted text matches the selected language, preventing cross-language mismatches before running analytics.
* **Smart Content Validation**: Enforces a strict validation pipeline (minimum word count thresholds + verb-presence checks) to ensure only valid sentence structures are analyzed.
* **Advanced Stylometric Metrics**:
  * Total word count & unique vocabulary calculation.
  * Lexical richness estimation (Type-Token Ratio variant).
  * Average sentence length analysis.
  * Most frequent meaningful words extraction (using `collections.Counter` to filter out stopwords and punctuation).
* **Dynamic Data Visualization**: Interactive charts powered by **Chart.js** rendered conditionally based on validation criteria.
* **Bento Grid / Glassmorphism UI**: Modern asymmetric dashboard aesthetic built with custom CSS variables, responsive design, and full multi-language localization dictionaries (`translations.py`).

---

## Tech Stack

* **Backend**: Python, Flask, Flask Sessions
* **NLP Engine**: spaCy (`es_core_news_sm`, `en_core_web_sm`, `fr_core_news_sm`, `it_core_news_sm`), langdetect
* **Frontend**: HTML5, Modern CSS3 (Glassmorphism & Bento Layouts), Chart.js
* **Architecture**: Modular translation dictionaries and session-based error-handling pipelines.

---

## Installation & Running Locally

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/tu-usuario/stylo.git](https://github.com/tu-usuario/stylo.git)
   cd stylo

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies**:
   ```bash
   pip install flask spacy langdetect

4. **Download spaCy language models**:
   ```bash
   python -m spacy download en_core_web_sm
   python -m spacy download es_core_news_sm
   python -m spacy download fr_core_news_sm
   python -m spacy download it_core_news_sm

5. **Run the application**:
   ```bash
   python app.py


Open your browser and navigate to http://127.0.0.1:5000/.