import pandas as pd
import re
import string

df = pd.read_csv('data_ulasan_feature_selection.csv')

# angka
def remove_number(text):
    return re.sub(r"\d+", " ", text)

# pengulangan huruf
def remove_repeated_chars(text):
    return re.sub(r'(.)\1{2,}', r'\1', text)

# tanda baca
def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

# link dan karakter non-ASCII
def remove_links(text):
    text = text.replace('\\t', " ").replace('\\n', " ").replace('\\u', " ").replace('\\', "")
    # mention, link, dan hashtag
    text = ' '.join(re.sub("([@#][A-Za-z0-9]+)|(\w+:\/\/\S+)", " ", text).split())
    # URL
    text = text.replace("http://", " ").replace("https://", " ")
    # karakter non-ASCII
    return re.sub(r'[^\x00-\x7F]+', '', text)

df['Ulasan_cleaning'] = df['Ulasan'].apply(remove_number)
df['Ulasan_cleaning'] = df['Ulasan_cleaning'].apply(remove_repeated_chars)
df['Ulasan_cleaning'] = df['Ulasan_cleaning'].apply(remove_punctuation)
df['Ulasan_cleaning'] = df['Ulasan_cleaning'].apply(remove_links)

df.to_csv('data_ulasan_cleaning.csv', index=False)

total_ulasan = len(df)
print(f'Total data ulasan: {total_ulasan}')
