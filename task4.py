import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup


# with open("task.json","r") as f:
#     data=json.load(f)
#     for i in data:
#         print(i)
#         url=i["url"]
#         print(url)

# def scrape_movie_details(movie_url):
#     movie_data={}
#     rec_url=requests.get(movie_url)
#     soup=BeautifulSoup(rec_url.text,"html.parser")
#     movie_name= soup.find("h1",attrs={"data-testid":"hero-title-block__title"}).text
#     movie_data["name"]=movie_name
#     print(movie_data)

#     # director=[]
#     # direct_name=soup.find("div",attrs={"data-testid":"shoveler"})
#     # b=direct_name.find('div',class_="ipc-shoveler__arrow")
#     # c=b.find("svg",class_="ipc-icon ipc-icon--chevron-right-inline ipc-icon--inline ipc-pager-icon")
#     # d=c.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-all sc-11eed019-10 fcovio ipc-metadata-list--base")
#     # e=d.find("li",class_="ipc-metadata-list__item")
#     # print(e)


# scrape_movie_details(url[0])


# #############################>>>>>>>>>>  (task-4)  <<<<<<<<<<<<<<<<<<<<<<################################


import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint


def scrape_movie_details(url):
    dict1 = {}
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    name = soup.find(
        "h1", attrs={"data-testid": "hero-title-block__title"}).text
    dict1["name"] = name
    g = []
    director_name = soup.find(
        'div', class_="ipc-metadata-list-item__content-container")
    x = director_name.find_all("li", class_="ipc-inline-list__item")
    for i in x:
        g.append(i.a.get_text())

    dict1["director"] = g
    country_name = soup.find(
        "li", attrs={"data-testid": "title-details-origin"}).find("a").text
    dict1["country"] = country_name
    j = []
    language_name = soup.find(
        "li", attrs={"data-testid": "title-details-languages"})
    x = language_name.find_all("li", class_="ipc-inline-list__item")
    for i in x:
        j.append(i.a.get_text())
    dict1["language"] = j
    poster_image_url = soup.find("img", class_="ipc-image")["src"]
    dict1["poster image url"] = poster_image_url
    bio = soup.find("span", attrs={"data-testid": "plot-xs_to_m"}).text
    dict1["bio"] = bio
    genre = soup.find("li", attrs={"data-testid": "storyline-genres"})
    Genre = genre.find_all("a")
    h = []
    dict1["genre"] = h
    for i in Genre:
        l = i.text
        h.append(l)
    run_time = soup.find(
        "li", attrs={"data-testid": "title-techspec_runtime"}).text.strip("Runtime")
    w = run_time.split(" ")
    print(w)
    if len(w) == 4:
        m = int(w[0])*60+int(w[2])
        print(m)
    else:
        m = int(m[0])*60
    dict1["runtime"] = m
    return (dict1)  # ..................................


with open("task.json", "r") as obj:
    gh = json.load(obj)
    all_data = []
    for j in gh:
        pr = j["url"]
        x = scrape_movie_details(pr)
        all_data.append(x)
        with open("task4.json", "w") as p:
            json.dump(all_data, p, indent=4)
