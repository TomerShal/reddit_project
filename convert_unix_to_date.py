# convert the unix timestamp to datetime

import pandas as pd
# from datetime import datetime

colnames = ['text', 'id', 'subreddit', 'meta', 'time', 'author', 'ups', 'downs', 'authorlinkkarma',
            'authorcommentkarma', 'authorisgold']
df = pd.read_csv("/Users/Tomer/Documents/Reddit Project/data/comments.csv", names=colnames)
df = df[pd.notnull(df['text'])]  # drop text null rows
df = df.reset_index() # reset the row indexing after removing nulls
df.time = df.time.astype(int)  # convert time column to integer
df.time = pd.to_datetime(df.time, unit='s')  # convert time from unix to datetime
print(df.time.head())
df.to_csv("/Users/Tomer/Documents/Reddit Project/data/comments_time_as_datetime.csv", index = False) # save to csv
