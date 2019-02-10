from nltk.corpus import wordnet

syn=wordnet.synsets('snub')[0]
print(syn.name())
print(syn.definition())
print(syn.pos())
lemmas=syn.lemmas()
print(len(lemmas))
print(lemmas[1].name())

#how to check similarity between tword in wordnet

from nltk.corpus import wordnet

syn= wordnet.synsets('allow')[0]
lemmas=syn.lemmas()
print(lemmas)
print(len(lemmas))
cb=wordnet.synsets('permit')[0]
ci=wordnet.synsets('let')[0]
print(cb.wup_similarity(ci))

