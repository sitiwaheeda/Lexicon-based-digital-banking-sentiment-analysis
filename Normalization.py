import pandas as pd
import ast

indo_slang_word_url = "https://raw.githubusercontent.com/nasalsabila/kamus-alay/master/colloquial-indonesian-lexicon.csv"
indo_slang_word = pd.read_csv(indo_slang_word_url)

def normalize_tokens(tokens):
    normalized_tokens = []
    for token in tokens:
        external_match = indo_slang_word[indo_slang_word['slang'] == token]
        if not external_match.empty:
            normalized_tokens.append(external_match['formal'].values[0])
        else:
            normalized_tokens.append(token)
    return normalized_tokens

df = pd.read_csv('/work/data_ulasan_stemming.csv')

def ensure_list_format(text):
    try:
        return ast.literal_eval(text) if isinstance(text, str) else text
    except (ValueError, SyntaxError):
        return []

df['Ulasan_stemming'] = df['Ulasan_stemming'].apply(ensure_list_format)
df['Ulasan_normalisasi'] = df['Ulasan_stemming'].apply(normalize_tokens)
df.to_csv('/work/data_ulasan_normalisasi.csv', index=False)

print(f'Total data ulasan: {len(df)}')
