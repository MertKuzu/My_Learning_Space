import requests
from bs4 import BeautifulSoup

#I learned web scraping. I'm getting the data with web scraping here.

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
list = soup.find("tbody", {"class":"lister-list"}).find_all("tr")
count = 1

for tr in list:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    year = tr.find("td", {"class":"titleColumn"}).find("span").text
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
    print(f"{count}. Film: {title.ljust(70)} Yıl: {year}  Puan: {rating}")
    count+=1
