import json
from pprint import pprint

with open('task.json','r') as f:
    data = json.load(f)
    lis=[]
    for i in data:
        if i['year'] not in lis:
            lis.append(i['year'])
    lis.sort()
    lis2=[]
    for j2 in lis:
        n=str(j2)[:-1]
        if n not in lis2:
            lis2.append(n)
    lis3=[]
    for j3 in lis2:
        lis3.append(int(j3)*10)
    print(lis3)
    dic={}
    for j in lis3:
        lic1=[]
        for j1 in data:
            if str(j)[:-1] in str(j1['year']):
                lic1.append(j1)
        dic[j]=lic1
    with open('task3.json','w') as f1:
        json.dump(dic,f1,indent=4)
    
        
        
        
        
        
        
        