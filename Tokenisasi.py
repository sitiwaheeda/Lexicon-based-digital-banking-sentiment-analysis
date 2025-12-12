import string
import re
import nltk
from nltk.tokenize import word_tokenize

# Download the required NLTK data
nltk.download('punkt_tab')

df = pd.read_csv('data_ulasan_case_folding.csv')
df['Ulasan_case_folding'] = df['Ulasan_case_folding'].fillna('')

def word_tokenize_wrapper(text):
    return word_tokenize(text)

df['Ulasan_tokenize'] = df['Ulasan_case_folding'].apply(word_tokenize_wrapper)
df.to_csv('data_ulasan_tokenize.csv', index=False)

print(f'Total data ulasan: {len(df)}')
