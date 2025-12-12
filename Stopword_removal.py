import pandas as pd

InSetp = pd.read_csv('/work/positive.csv')  # InSet Lexicon Positive
InSetn = pd.read_csv('/work/negative.csv')  # InSet Lexicon Negative
stopword_dict = pd.read_csv('/work/stopwords_indonesian.txt', header=None, names=['word'])  #NLTK STOPWORD

all_words_set = set(InSetp['word']).union(set(InSetn['word']))

stopword_dict_filtered = stopword_dict[~stopword_dict['word'].isin(all_words_set)]

with open('stopwords_indonesian_modified.txt', 'w') as f:
    f.write("\n".join(stopword_dict_filtered['word']))
