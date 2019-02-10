from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords

stemmer=PorterStemmer()
print(stemmer.stem('playing'))

word=open('Incident_Miner.txt')
word=word.read()
word_token=word_tokenize(word)


english_stop= set(stopwords.words('english'))
new_word=[]

for i in word_token :
    if i not in english_stop and len(i)>2 :
        new_word.append(i.lower())
stemmer=PorterStemmer()
new_word=stemmer.stem(new_word)
c=Counter(new_word)
print(c.most_common(20)


