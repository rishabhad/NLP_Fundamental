import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from  nltk.corpus import stopwords
from  nltk.tokenize import sent_tokenize,word_tokenize

train = pd.read_csv('train.csv',encoding='iso-8859-1')
#print(train.head(10))
print(train.info())
print(train['SentimentText'][400])

print(train['SentimentText'].str.len().mean())
print(train['SentimentText'].str.len().std())
label=[0,1]

sentiment_count=[train['Sentiment'].value_counts()[0],train['Sentiment'].value_counts()[1]]
#print(sentiment_count)
'''plt.plot(sentiment_count)
fig1, ax1 = plt.subplots()
ax1.bar(sentiment_count,labels=label)
plt.title('Bar Chart')
#plt.show()'''
stopWords = set(stopwords.words('english'))
train.SentimentText = [w for w in train['SentimentText'] if w.lower() not in stopWords]

#print(type(train))
train.SentimentText=[word_tokenize(w) for w in train['SentimentText']]

train=[w.lower() for i in train for w in i]

train=[w for w in train if w not in stopWords and len(w)>2]
train=[w for w in train if w.isalpha()]
ps=nltk.PorterStemmer()
train=[ps.stem(w)  for w in train]
print(type(train))

#print(train[:50])

X=train['SentimentText']
y = train['Sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

train1=pd.concat([X_train,y_train], axis=1)

print(train.shape)'''




