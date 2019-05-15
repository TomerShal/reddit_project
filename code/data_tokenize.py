import string
import pandas as pd
from nltk.tokenize import word_tokenize

comments = pd.read_csv(r'C:\Users\tomer.shalhon\Desktop\comments_no_duplicates.csv')

for i in range(0, len(comments)):
    s = comments.loc[comments.index[i], 'text']
    s = s.translate(str.maketrans('', '', string.punctuation)) ## Remove punctuation
    s = s.strip() ## Remove whitespaces
    tokens = word_tokenize(s) ## divide comment into tokens

