import pandas as pd
import nltk
import nltk.tokenize as nt
import nltk.corpus as nl
import nltk.stem as ps
import sklearn.feature_extraction.text as tf
import sklearn.cluster as km
import matplotlib.pyplot as plt
import csv
import collections
import tweepy
import csv

stopword_list = list(set(nl.stopwords.words('english')))

ps = ps.PorterStemmer()
def generate_tfidf(text_corpora):
    vectorizer = tf.TfidfVectorizer(lowercase=False)
    vectorizer.fit(text_corpora)
    vector = vectorizer.transform(text_corpora)
    return vector
stopword_list = list(set(nl.stopwords.words('english')))
r_df = pd.read_csv("python4.csv",encoding = "ISO-8859-1")
print(r_df)


text_corpora = [s.translate(str.maketrans("","","0123456789")) for s in r_df.loc[:,"scraptweets"]]
words_data = [nt.word_tokenize(s.lower()) for s in text_corpora]
words_data = [[ ps.stem(word) for word in sent if word not in stopword_list ] for sent in words_data  ]
sent_data  = [" ".join(sent) for sent in words_data]

vector = generate_tfidf(sent_data)

kmeans_obj = km.KMeans(n_clusters = 5, max_iter=100)
clusters = kmeans_obj.fit(vector)

r_df["label"]=clusters.labels_  
print("cluster 1")

r_df.loc[r_df["label"]==0]
print(r_df.loc[r_df["label"]==1])
r_df.to_csv("Clustered_tweet2.txt",index=False)

file = open('Clustered_tweet1.txt', encoding="utf8",)
a= file.read()
stopword_list = list(set(nl.stopwords.words('english')))

wordCount = {}
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("-","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopword_list:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
n_print = 2
d=[]
word_counter = collections.Counter(wordCount)
for word, count in word_counter.most_common(n_print):
    d.append(word)
print(d)

print("cluster 2")

r=r_df.loc[r_df["label"]==1]
print(r_df.loc[r_df["label"]==1])
r_df.to_csv("Clustered_tweet2.txt",index=False)

file = open('Clustered_tweet2.txt', encoding="utf8")
a= file.read()
stopword_list = list(set(nl.stopwords.words('english')))

wordCount = {}
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("-","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopword_list:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
n_print = 10
a=[]
word_counter = collections.Counter(wordCount)
for word, count in word_counter.most_common(n_print):
    a.append(word)
print(a)

print("cluster 3")
r=r_df.loc[r_df["label"]==2]
print(r_df.loc[r_df["label"]==2])
r_df.to_csv("Clustered_tweet2.txt",index=False)

file = open('Clustered_tweet2.txt', encoding="utf8")
a= file.read()
stopword_list = list(set(nl.stopwords.words('english')))

wordCount = {}
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("-","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopword_list:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
n_print = 10
a=[]
word_counter = collections.Counter(wordCount)
for word, count in word_counter.most_common(n_print):
    a.append(word)
print(a)

print("cluster 4")

r=r_df.loc[r_df["label"]==3]
print(r_df.loc[r_df["label"]==3])
r_df.to_csv("Clustered_tweet3.txt",index=False)

file = open('Clustered_tweet3.txt', encoding="utf8")
a= file.read()
stopword_list = list(set(nl.stopwords.words('english')))

wordCount = {}
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("-","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopword_list:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
n_print = 10
a=[]
word_counter = collections.Counter(wordCount)
for word, count in word_counter.most_common(n_print):
    a.append(word)
print(a)

print("cluster 5")
r=r_df.loc[r_df["label"]==4]
print(r_df.loc[r_df["label"]==4])
r_df.to_csv("Clustered_tweet4.txt",index=False)

file = open('Clustered_tweet4.txt', encoding="utf8")
a= file.read()
stopword_list = list(set(nl.stopwords.words('english')))

wordCount = {}
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")  
    word = word.replace("!","")
    word = word.replace("-","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopword_list:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
nPrint = 10
a=[]
wordCounter = collections.Counter(wordCount)
for word, count in wordCounter.most_common(nPrint):
    a.append(word)
print(a)