import requests,json
from bs4 import BeautifulSoup
from pprint import pprint



main_url = "https://www.imdb.com"
URL = "https://www.imdb.com/india/top-rated-indian-movies/"
rec_link=requests.get(URL)
soup=BeautifulSoup(rec_link.text,"html.parser")

def scrap_movie_details():
    main_div= soup.find('div',class_='lister')
    tbody= main_div.find('tbody',class_='lister-list')
    trs= tbody.find_all('tr')

    movie_rank=[]            # all in integer
    movie_names=[]            # all in string
    year_of_relese=[]        # all in integer
    movie_ratings=[]         # all in float
    movie_urls=[]            # all urls of movies

    for tr in trs:
        position=tr.find("td", class_="titleColumn").get_text().strip()     # strip--space menten ke lie
        rank=''
        for i in position:
            if '.' not in i:
                rank+=i
            else:
                break
        movie_rank.append(rank)

        title=tr.find('td',class_="titleColumn").a.get_text()         #'a' ka matb 'a' tankar ke undar
        movie_names.append(title)

        year=tr.find('td',class_="titleColumn").span.get_text()       # 'span ka matb 'span' tank ke undar
        year_of_relese.append(year)

        imdb_rating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)

        link=tr.find('td',class_="titleColumn").a['href']
        movie_link="https://www.imdb.com"+link  
        movie_urls.append(movie_link)
    Top_movie=[]
    details= { "position": "", "name":"" ,"year":"", "rating":"", "url": ""}
    for i in range(0,len(movie_rank)):
        details["position"]=int(movie_rank[i])
        details["name"]    =str(movie_names[i])
        year_of_relese[i]  =year_of_relese[i][1:5]
        details["year"]    =int(year_of_relese[i])
        details["rating"]  =float(movie_ratings[i])
        details["url"]     =movie_urls[i]
        Top_movie.append(details)

        details= { "position": "", "name":"" ,"year":"", "rating":"", "url": ""}
    
    with open("task.json","w") as f:
        json.dump(Top_movie,f, indent=4)
    return Top_movie 
pprint(scrap_movie_details())



# task3


# import json
# from pprint import pprint

# with open('task.json','r') as f:
#     data = json.load(f)
#     lis=[]
#     for i in data:
#         if i['year'] not in lis:
#             lis.append(i['year'])
#     lis.sort()
#     lis2=[]
#     for j2 in lis:
#         n=str(j2)[:-1]
#         if n not in lis2:
#             lis2.append(n)
#     lis3=[]
#     for j3 in lis2:
#         lis3.append(int(j3)*10)
#     print(lis3)
#     dic={}
#     for j in lis3:
#         lic1=[]
#         for j1 in data:
#             if str(j)[:-1] in str(j1['year']):
#                 lic1.append(j1)
#         dic[j]=lic1
#     with open('task1.json','w') as f1:
#         json.dump(dic,f1,indent=4)
