from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    # print("{:-<40} {}".format(sentence, str(score)))
    return score['compound']

comments = pd.read_csv(r'C:\Users\tomer.shalhon\Desktop\comments_no_duplicates.csv')
sentiment_score = pd.DataFrame(columns=('text', 'sentiment_score','ups', 'downs'))

sentiment_score['text'] = comments['text']
sentiment_score['ups'] = comments['ups']
sentiment_score['downs'] = comments['downs']
for i in range(0, len(comments)):
    sentiment_score.loc[comments.index[i], 'sentiment_score'] = sentiment_analyzer_scores(comments.iloc[i]['text'])
    print(i,':',sentiment_analyzer_scores(comments.iloc[i]['text']))


sentiment_score.to_csv(r'C:\Users\tomer.shalhon\Desktop\sentiment.csv', index=False)

