from bs4 import BeautifulSoup
import requests

# with open("website.html","r",encoding="utf-8") as fp:
#     contents = fp.read()

# soup = BeautifulSoup(contents,"html.parser")

# print(soup.title.name)

# response = requests.get("https://news.ycombinator.com/")
# web_page_contents = response.text

# soup = BeautifulSoup(web_page_contents,"html.parser")

# anchor_tags = soup.select(selector="span.titleline>a")
# print(len(anchor_tags))

# points_tags = soup.select(selector="span.score")

# print(len(points_tags))

# for tag in points_tags:
#     print(tag.getText()) 

#top 100 movies

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_data = response.text

soup = BeautifulSoup(website_data,"html.parser")

movie_tags = soup.select(selector="h3.title")

movie_titles = []

for movie in movie_tags:
    movie_titles.append(movie.getText())

with open("movies.txt","a",encoding="utf-8") as fp:
    for i in range(len(movie_titles)-1, -1, -1):
        fp.write(movie_titles[i])
        fp.write("\n")

    



