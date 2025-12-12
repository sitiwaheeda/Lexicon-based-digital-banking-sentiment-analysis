pip install Sastrawi #install sastrawi first

import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import word_tokenize
import nltk
import ast

nltk.download('punkt')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

df = pd.read_csv('/work/data_ulasan_tokenize.csv')

def convert_to_list(text):
    if isinstance(text, str):
        try:
            return ast.literal_eval(text)
        except (ValueError, SyntaxError):
            return text.split()
    return text

def stem_tokens(tokens):
    return [stemmer.stem(token) for token in tokens]

df['Ulasan_tokenize'] = df['Ulasan_tokenize'].apply(convert_to_list)
df['Ulasan_stemming'] = df['Ulasan_tokenize'].apply(stem_tokens)
df.to_csv('/work/CASE 1/data_ulasan_stemming.csv', index=False)

print(f'Total data ulasan: {len(df)}')
