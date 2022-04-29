import json,requests
from bs4 import BeautifulSoup
from pprint import pprint

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

x=scrape_movie_details("https://www.imdb.com/title/tt0986264/")
with open("task5.json","w") as p:
    json.dump(x,p,indent=4)
    

with open("task5.json","r") as p:
    d=json.load(p)
movies=[]
for i in range(10):
    movies.append(d[i]["url"])

def get_movie_list_details(movies):
    movies_details=[]
    for i in movies:
        movies_details.append(scrape_movie_details(i))
    return (movies_details)
x=get_movie_list_details(movies)
print("successfully run")
with open("task5.json","w") as m:
    json.dump(x,m,indent=6)