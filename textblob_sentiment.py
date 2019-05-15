from textblob import TextBlob
import pandas as pd

comments = pd.read_csv(r'C:\Users\tomer.shalhon\Desktop\comments_no_duplicates.csv')
sentiment_score = pd.DataFrame(columns=('text', 'polarity','ups', 'downs'))

sentiment_score['text'] = comments['text']
sentiment_score['ups'] = comments['ups']
sentiment_score['downs'] = comments['downs']

for i in range(0, len(comments)):
    sentiment_score.loc[comments.index[i], 'polarity'] = TextBlob(comments.iloc[i]['text']).sentiment.polarity
    print(i,':',TextBlob(comments.iloc[i]['text']).sentiment.polarity)

sentiment_score.to_csv(r'C:\Users\tomer.shalhon\Desktop\text_blob_sentiment.csv', index=False)
