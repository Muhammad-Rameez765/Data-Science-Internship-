df['Genre'].dtype

list1=[]
for value in df['Genre']:
    list1.append(value.split(','))
    
df['temp']=list1

len(df[df['Genre'].str.contains('Action',case=False)])

list1

d1 = []

for item in list1:
    for item1 in item:
        d1.append(item1)
        
        
uni_list = []
for item in d1:
    if item not in uni_list:
        uni_list.append(item1)
        
        
len(uni_list)


uni_list


Counter(d1)