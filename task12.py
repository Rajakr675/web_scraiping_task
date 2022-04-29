import json,requests,pprint
from bs4 import BeautifulSoup

with open("task.json","r") as boj:
        d = json.load(boj)
def scrape_movie_cast(movie_cast):
        cast=requests.get(movie_cast)
        soup=BeautifulSoup(cast.text,"html.parser")
        info=soup.find("table",class_="cast_list")
        cast1=info.find_all("tr")
        imdb_list=[]
        for t in cast1:
            td=t.find("td",class_="")
            if td!=None:
                cast_dict={}
                name=td.find("a").text
                imdb_id=td.find("a")["href"][6:15]
                cast_dict["name"]=name.strip()
                cast_dict["imdb_id"]=imdb_id
                imdb_list.append(cast_dict)
        return imdb_list
var = scrape_movie_cast(d[0]['url']+"fullcredits?ref=ttcl_sm#cast")
print(var)
with open("task12.json","w") as obj1:
        json.dump(var,obj1,indent=6)