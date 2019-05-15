import string
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

comments = pd.read_csv(r'C:\Users\tomer.shalhon\Desktop\comments_no_duplicates.csv')
stop_words = set(stopwords.words('english'))

for i in range(0, len(comments)):
    s = comments.loc[comments.index[i], 'text']
    s = s.translate(str.maketrans('', '', string.punctuation)) ## Remove punctuation
    s = s.strip() ## Remove whitespaces
    s_tokenized = word_tokenize(s) ## divide comment into tokens
    s_filtered = []
    for word in s_tokenized:
        if word not in stop_words:
            s_filtered.append(word) ## remove stop words from tokenized comment
    comments['text_processed'][i]  = s_filtered
    print(i,': true')

comments.to_csv(r'C:\Users\tomer.shalhon\Desktop\comments_pre_process.csv', index=False) ## write to csv















