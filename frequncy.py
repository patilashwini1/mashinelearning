import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus.reader.wordnet import WordNetError
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


ps = PorterStemmer()


def generate_tfidf(text_corpora):
    
    
    vectorizer = TfidfVectorizer(lowercase=False)

    vectorizer.fit(text_corpora)

    vector = vectorizer.transform(text_corpora)

    return vector


stopword_list = list(set(stopwords.words('english')))

r_df = pd.read_csv("clean_tweets.csv")




text_corpora = [s.translate(str.maketrans("","","0123456789")) for s in r_df.loc[:,"clean_txt"]]
words_data = [word_tokenize(s.lower()) for s in text_corpora]

words_data = [[ ps.stem(word) for word in sent if word not in stopword_list ] for sent in words_data  ]
sent_data  = [" ".join(sent) for sent in words_data]


vector = generate_tfidf(sent_data)

kmeans_obj = KMeans(n_clusters = 2, max_iter=100,verbose=0,random_state=1)
clusters = kmeans_obj.fit(vector)

r_df["label"] = clusters.labels_

print(“cluster 1”)
Print(r_df.loc[r_df[“label”]==0])

print(“cluster 2”)
prin(r_df.loc[r_df[“label”]==1)		

print("Completed!")