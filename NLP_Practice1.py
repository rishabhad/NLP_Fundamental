para='Hello everyone Good Morning.How was your day.I need one help from everyone.Please mark your attendance'

#how to tokenize sentence from para
from nltk.tokenize import sent_tokenize

#print(sent_tokenize(para))

#how to tokenize 

from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("[\w']+")
word=tokenizer.tokenize("Can't is a contraction")

tokenizer=RegexpTokenizer("[\s'.]+",gaps=True)
#print(tokenizer.tokenize("Can't is a contraction."))

from nltk.corpus  import stopwords

english_stop= set(stopwords.words('english'))
print(word)
print([i for i in word if i not in english_stop])

