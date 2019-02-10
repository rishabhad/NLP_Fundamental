exp="Hey This is Rishabh"
sent=[]

for x in exp:
    x=x.split(" ")
    sent.append('-'.join(x))
sent=''.join(sent)
print(sent)
