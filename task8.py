


import json,requests,pprint,os
from bs4 import BeautifulSoup

url = "https://www.imdb.com/india/top-rated-indian-movies/"
r = requests.get(url)
bh = r.content
soup = BeautifulSoup(bh,"html.parser")
def scrap_top_list():
    main_div = soup.find("div",class_="lister")
    tbody = main_div.find("tbody",class_="lister-list")
    trs = tbody.find_all("tr")
    # print(trs)
    movie_rank =[]
    movie_name =[]
    year_of_release =[]
    movie_urls = []
    movie_ratings = []
    for tr in trs:
        position = tr.find("td",class_= "titleColumn").get_text().strip()
        # print(position)
        rank = ''
        for i in position:
            # print(i)
            if "." not in i:
                rank = rank + i
            else:
                break
        movie_rank.append(rank)
        # print(movie_rank)
        title = tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)
        year = tr.find("td",class_="titleColumn").span.get_text()
        year_of_release.append(year)
        imdb_rating = tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)
        link = tr.find("td",class_="titleColumn").a["href"]
        movie_link = "https://www.imdb.com"+link
        movie_urls.append(movie_link)
    Top_Movies = []
    details = {"name":"","year":"","rating":"","url":""}
    for i in range(0,len(movie_rank)):
        details["postion"] = int(movie_rank[i])
        details["name"] = str(movie_name[i])
        year_of_release[i] = year_of_release[i][1:5]
        details["year"] = int(year_of_release[i])
        details["rating"] = float(movie_ratings[i])
        details["url"] = movie_urls[i]
        Top_Movies.append(details)
        details = {"name":"","year":"","rating":"","url":""}
    return Top_Movies
p = (scrap_top_list())
print(p)
def scrape_movie_details(url):
    movie_id = " "
    for id in url[27:]:
        if "/" not in id:
            movie_id += str(id)
        else:
            break
    file_name = movie_id + ".json"
    text = None
    if os.path.exists(file_name):
        print("hello")
        g = open(file_name)
        text = g.read()
        return text
    if text is None:
        print("sorry")
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
        file1 = open(file_name,"w")
        v = json.dumps(dict1)
        file1.write(v)
        file1.close()
    return dict1
gh = p[1]["url"]
scrap = scrape_movie_details(gh)
print(scrap)





