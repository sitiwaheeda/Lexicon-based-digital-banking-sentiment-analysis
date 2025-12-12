lexicon_positive = dict()
import csv
with open('/work/positive.tsv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader)
    for row in reader:
        lexicon_positive[row[0]] = int(row[1])

lexicon_negative = dict()
with open('/work/negative.tsv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader)
    for row in reader:
        lexicon_negative[row[0]] = int(row[1])

def sentiment_analysis_lexicon_indonesia(tokens):
    score = 0
    sentiments = []
    for token in tokens:
        if token in lexicon_positive:
            sentiment = f"{token}(+{lexicon_positive[token]})"
            sentiments.append(sentiment)
            score += lexicon_positive[token]
        if token in lexicon_negative:
            sentiment = f"{token}({lexicon_negative[token]})"
            sentiments.append(sentiment)
            score += lexicon_negative[token]
    polarity = ''
    if score > 0:
        polarity = 'positive'
    elif score < 0:
        polarity = 'negative'
    else:
        polarity = 'neutral'
    return score, polarity, ', '.join(sentiments)

import pandas as pd

df = pd.read_csv('/work/CASE 1/data_ulasan_preprocessing.csv')
df['Ulasan_preprocessing'] = df['Ulasan_preprocessing'].apply(eval)
df['Sentiment_Score'], df['Sentiment_Polarity'], df['Sentiment_Detail'] = zip(*df['Ulasan_preprocessing'].apply(sentiment_analysis_lexicon_indonesia))
df = df[['Ulasan_preprocessing', 'Sentiment_Score', 'Sentiment_Polarity', 'Sentiment_Detail']]

df.to_csv('/work/CASE 1/sentiment_analysis.csv', index=False)
