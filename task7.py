
# import json
# from pprint import pprint



# with open("task5.json","r") as f:
#     d= json.load(f)

# def analyse_movies_directors():
#     dic={}
#     for i in d:
#         for y in i["director"]








  

# webscraping task 7

import json  
from pprint import pprint 

with open("task4.json") as p:
    d=json.load(p)

def analyse_movies_directors():
    dic={}
    for i in d:
        for y in i["director"]:
            print(y)
            if y in dic:
                dic[y]+=1
            else:
                dic[y]=1
    return dic
pprint(analyse_movies_directors())