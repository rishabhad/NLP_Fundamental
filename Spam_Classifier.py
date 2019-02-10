import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import chardet 
from collections import Counter 
from  sklearn import feature_extraction,model_selection,naive_bayes,metrics,svm

with open("spam.csv" ,'rb') as rawdata:
	result= chardet.detect(rawdata.read())

#print(result)
data=pd.read_csv('spam.csv' , encoding='Windows-1252')

print(data.info())

count_class=pd.value_counts(data["v1"], sort=True)
#print(count_class)

count_class.plot(kind='Bar',color=["blue","orange"])
plt.title('Bar Chart')
#plt.show()
'''df = data[data['v1']=='ham']['v2']
df=df.values
df.reshape(-1,1)
df=df.tolist()

count1=Counter(df).most_common(20)
#print(count1)

df1 = data[data['v1']=='spam']["v2"]
df1=df1.values
df1.reshape(-1,1)
df1=df1.tolist()
df1=[i.split() for i in df1]

count2=Counter(df1).most_common(20)
df1=pd.DataFrame.from_dict(count2)'''
#print(df1)


count1 = Counter(" ".join(data[data['v1']=='ham']["v2"]).split()).most_common(20)
df1 = pd.DataFrame.from_dict(count1)
#print(df1)
df1 = df1.rename(columns={0: "words in non-spam",1 : "count"})
count2 = Counter(" ".join(data[data['v1']=='spam']["v2"]).split()).most_common(20)
df2 = pd.DataFrame.from_dict(count2)
df2 = df2.rename(columns={0: "words in spam",1 : "count_"})

df1.plot.bar(legend = True)
y_pos = np.arange(len(df1["words in non-spam"]))
print(y_pos)
plt.xticks(y_pos, df1["words in non-spam"])
plt.title('More frequent words in non-spam messages')
plt.xlabel('words')
plt.ylabel('number')
plt.show()

df2.plot.bar(legend = False, color = 'orange')
y_pos = np.arange(len(df2["words in spam"]))
plt.xticks(y_pos, df2["words in spam"])
plt.title('More frequent words in spam messages')
plt.xlabel('words')
plt.ylabel('number')
plt.show()






