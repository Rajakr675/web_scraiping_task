
# --------------task_3------------------------------

  
import json
from pprint import pprint

with open('task.json','r') as f:
    data = json.load(f)
    lis=[]
    for i in data:
        if i['year'] not in lis:
            lis.append(i['year'])
    lis.sort()
    dic={}
    for j in lis:
        lic1=[]
        for j1 in data:
            if j == j1['year']:
                lic1.append(j1)
        dic[j]=lic1

    pprint(dic)


