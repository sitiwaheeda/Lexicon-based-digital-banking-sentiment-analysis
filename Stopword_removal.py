import pandas as pd
import nltk
import ast  

nltk.download('punkt')

with open('/work/stopwords_indonesian_modified.txt', 'r') as f:
    stopwords = set(f.read().splitlines())
df = pd.read_csv('/work/CASE 1/data_ulasan_normalisasi_final.csv')

def convert_to_list(text):
    if isinstance(text, str):
        try:
            return ast.literal_eval(text)  
        except (ValueError, SyntaxError):
            return text.split() 
    return text


def remove_stopwords(tokens):
    return [token for token in tokens if token not in stopwords]

df['Ulasan_normalisasi_final'] = df['Ulasan_normalisasi_final'].apply(convert_to_list)
df['Ulasan_stopword'] = df['Ulasan_normalisasi_final'].apply(remove_stopwords)
df.to_csv('/work/CASE 1/data_ulasan_stopword.csv', index=False)


total_ulasan = len(df)
print(f'Total data ulasan: {total_ulasan}')
