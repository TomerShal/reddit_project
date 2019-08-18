import pandas as pd

textblob = pd.read_csv(r'C:\Users\tomer.shalhon\Desktop\text_blob_sentiment.csv')
vader = pd.read_csv(r'C:\Users\tomer.shalhon\Desktop\sentiment.csv')

combined = pd.merge(textblob, vader, on='text', how="outer")
sentiment_combined = pd.DataFrame(columns=('text', 'textblob_sentiment_score','vader_sentiment_score', 'average_sentiment_score'))

sentiment_combined['text'] = combined['text']
sentiment_combined['textblob_sentiment_score'] = combined['polarity']
sentiment_combined['vader_sentiment_score'] = combined['sentiment_score']
sentiment_combined['average_sentiment_score'] = ((combined['polarity'] + combined['sentiment_score'])/2)

sentiment_combined.to_csv(r'C:\Users\tomer.shalhon\Desktop\sentiment_combined.csv', index=False)
