'''import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_,spacy.explain(ent.label_))'''


import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'San Francisco considers banning sidewalk delivery robots')

# document level
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print(ents)

# token level
ent_san = [doc[0].text, doc[0].ent_iob_, doc[0].ent_type_]
ent_francisco = [doc[1].text, doc[1].ent_iob_, doc[1].ent_type_]
print(ent_san)  # [u'San', u'B', u'GPE']
print(ent_francisco)  # [u'Francisco', u'I', u'GPE']
