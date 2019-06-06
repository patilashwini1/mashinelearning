# import twitter
# import json
# import pandas as pd
# import csv
# import nlt.corpus as nl
        

#         with open('cluster2.txt') as csv_file:
#         csv_reader = csv.DictReader(csv_file, delimiter=',')
#         stopword_list = list(set(nl.stopwords.words('english')))
#         for tweet in reader:
#             for word in tweet.lower().split():
#                 word = word.replace(".","")
#                 word = word.replace(",","")
#                 word = word.replace(":","")
#                 word = word.replace("\"","")
#                 word = word.replace("!","")
#                 word = word.replace("â€œ","")
#                 word = word.replace("â€˜","")
#                 word = word.replace("*","")
#                 if word not in stopwords:
#                     if word not in wordcount:
#                         wordcount[word] = 1
#                     else:
#                         wordcount[word] += 1
#         print(tweet)


import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'iqrLxWicFMDxiG7LEQMnUgzfK'
consumer_secret = '7WaJiNzBguedhOQ5SsKIuc77XCLH6Gg353N0Y2byyo5fLWe3ie'
access_token = '1129014635607183360-88lX5VPPWjImRGnuaeYxFdmwdkJU7U'
access_token_secret ='9Zs2JSAvXUV1pQ2PKw5aOos4crwljdtWdVyyRBiAtGxP8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
# csvFile = open('python.csv', 'a')
# #Use csv Writer
# csvWriter = csv.writer(csvFile)
hashtag=input("enter you want to serach=")

stratDate=input("enter you want start date=")
for tweet in tweepy.Cursor(api.search,q=hashtag,lang="en",since=stratDate).items(1000):
    s=[tweet.created_at, tweet.text.encode('utf-8')]
    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    with open('people3.csv', 'a') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(s)
