# 📊 Lexicon-Based Sentiment Analysis of LINE Bank App Reviews Natural Language Processing (NLP)

## 📌 Project Overview

This project implements a lexicon-based sentiment analysis model on 25,144 Indonesian user reviews of the LINE Bank app collected from the Google Play Store (2021–2024). The goal is to identify sentiment patterns—positive, neutral, and negative—using a full NLP preprocessing pipeline and the InSet Indonesian Sentiment Lexicon.

## 🎯 Objectives

- Classify user reviews into positive, neutral, and negative categories using a lexicon-based method.
- Implement a complete NLP pipeline including cleaning, normalization, tokenization, and stemming.
- Apply the Indonesian InSet Lexicon to compute sentiment scores.
- Validate the sentiment classifications through manual labeling and multi-class evaluation metrics.
- Analyze sentiment distribution trends from a large-scale dataset.

## 🧠 Methodology

### 1. Dataset
- Source: Google Play Store
- Reviews: 25,144
- Language: Bahasa Indonesia
- Collected using: Google Play Scraper (Python)

### 2. Preprocessing
The preprocessing follows 7 NLP stages:
| Step                  | Description                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------ |
| **Feature Selection** | Extracts the *content* field from raw review metadata.                                     |
| **Cleaning**          | Removes numbers, punctuation, URLs, emojis, repeated characters, etc.                      |
| **Case Folding**      | Converts all text to lowercase.                                                            |
| **Tokenization**      | Uses NLTK to split text into individual tokens.                                            |
| **Stemming**          | Uses **Sastrawi** Indonesian stemmer.                                                      |
| **Normalization**     | Converts slang/abbreviations using external + custom lexicon.                              |
| **Stopword Removal**  | Removes Indonesian stopwords; modified to avoid removing adjectives relevant to sentiment. |

### 3. Sentiment Classification

Sentiment classification uses:
- InSet (Indonesian Sentiment) Lexicon
- Word scoring scheme:
  - +1 to +2 → Positive
  - 0 → Neutral
  - −1 to −2 → Negative

Classification logic:
```
┌────────────────────────────────────┐
│  Total Score > 0 → Positive        │
│  Total Score < 0 → Negative        │
│  Total Score = 0 → Neutral         │
└────────────────────────────────────┘
```

### 4. Model Validation

10% of the dataset (random sampling) was manually labeled to evaluate accuracy.
Evaluation metrics (multi-class):
- Accuracy
- Precision
- Recall
- F1-Score (Weighted Average)

## 📈 Results
Sentiment Distribution
- Negative: 61.9%
- Positive + Neutral: 38.1%

Model Performance
| **Metric**    | **Netral** | **Positif** | **Negatif** | **Weighted Avg** |
| ------------- | ---------: | ----------: | ----------: | ---------------: |
| **Accuracy**  |          — |           — |           — |         **0.71** |
| **Precision** |       0.43 |        0.70 |        0.76 |         **0.69** |
| **Recall**    |       0.24 |        0.64 |        0.89 |         **0.71** |
| **F1-Score**  |       0.31 |        0.67 |        0.82 |         **0.70** |

## 🛠️ Technologies Used

- Python 3.x
- Pandas, NumPy
- NLTK
- Sastrawi Stemmer
- Matplotlib
- WordCloud
- Google Play Scraper

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.

## 🧪 Visualizations

The project includes:

### Sentiment distribution charts

<img width="381" height="382" alt="sentiment distribution" src="https://github.com/user-attachments/assets/400fe45e-2779-4d04-aa11-75717c4680ca" />


### Word clouds for sentiment categories

- Negative sentiment
  
  <img width="790" height="405" alt="sentimen negative line bank" src="https://github.com/user-attachments/assets/a6731363-6ffd-44f8-adc4-31a13b471950" />

- Positive sentiment
  
  <img width="790" height="405" alt="sentimen positive line bank" src="https://github.com/user-attachments/assets/54d8ccc1-efda-45af-9605-b1aa68dc2730" />

- Netral sentiment
  
  <img width="790" height="405" alt="sentimen netral line bank" src="https://github.com/user-attachments/assets/00d8e0c4-d6ea-42d5-88ef-26f96cb49722" />

##Credits
```bash
https://raw.githubusercontent.com/nasalsabila/kamus-alay/master/colloquial-indonesian-lexicon.csv
```
