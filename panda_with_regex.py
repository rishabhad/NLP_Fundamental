import pandas as pd

data=pd.read_csv('Todolist.csv', header=None)


data=data.rename(columns={0:'task'})

print(data)

#print(data['task'].str.len())
#print(data['task'].str.rstrip().str.len())

#print(data['task'].str.contains('hold'))
#print(data['task'].str.count(r'\d'))
#print(data['task'].str.findall(r'\d'))
#print(data['task'].str.findall(r'(\d?\d):?(\d?)'))
print(data['task'].str.findall(r'(\w+day)'))
print(data['task'].str.replace(r'(\w+day)','????'))
