
import json,requests,os,pprint
from bs4 import BeautifulSoup

with open("task.json","r") as p:
    d=json.load(p)
def scrape_movie_details(url):
    dict1={}
    page= requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    name=soup.find("h1", attrs={"data-testid":"hero-title-block__title"}).text
    dict1["name"]=name
    g=[]
    director_name=soup.find('div', class_="ipc-metadata-list-item__content-container")
    x=director_name.find_all("li",class_="ipc-inline-list__item")
    for i in x:
        g.append(i.a.get_text()) 
    dict1["director"]=g
    country_name=soup.find("li",attrs={"data-testid":"title-details-origin"}).find("a").text
    dict1["country"]=country_name
    j=[]
    language_name=soup.find("li",attrs={"data-testid":"title-details-languages"})
    x=language_name.find_all("li",class_="ipc-inline-list__item")
    for i in x:
        j.append(i.a.get_text())
    dict1["language"]=j
    poster_image_url=soup.find("img",class_="ipc-image")["src"]
    dict1["poster image url"]=poster_image_url
    bio=soup.find("span",attrs={"data-testid":"plot-xs_to_m"}).text
    dict1["bio"]=bio
    genre=soup.find("li",attrs={"data-testid":"storyline-genres"})
    Genre=genre.find_all("a")
    h=[]
    dict1["genre"]=h
    for i in Genre:
        l=i.text
        h.append(l)
    run_time=soup.find("li",attrs={"data-testid":"title-techspec_runtime"}).text.strip("Runtime")
    w=run_time.split(" ")
    if len(w)==4:
        m=int(w[0])*60+int(w[2])
    else:
        m=int(m[0])*60
    dict1["runtime"]=m
    return (dict1)

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

def get_movie_list_details(movies):
    text=None
    file_name=d[0]['url'][28:-1]+"_cast.json"
    if os.path.exists(d[0]['url'][22:-1]+"cast.json"):
        print("hello")
        f=open(file_name)
        text=f.read()
        return text
    if text is None:
        print("sorry")
        x=scrape_movie_details(movies)
        y=d[0]['url']+"fullcredits?ref=ttcl_sm#cast"
        z=scrape_movie_cast(y)
        x["cast"]=z
        file1=open(file_name,"w")
        raw=json.dumps(x)
        file1.write(raw)
        file1.close()
        return (x)
m=get_movie_list_details(d[0]['url'])
pprint.pprint(m)
with open("task13.json","w") as ob:
    json.dump(m,ob,indent=6)