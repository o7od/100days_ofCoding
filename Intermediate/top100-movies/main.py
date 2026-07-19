import requests
from bs4 import BeautifulSoup

imdb_top_movies = requests.get("https://www.tcm.com/articles/afi-top-100")

soup = BeautifulSoup(markup=imdb_top_movies.text, features="html.parser")

movies = soup.find_all(name="a", class_="card-button usePointer")

top_movies = [movie.get("aria-label") for movie in movies]

with open("top_100_movies.txt", mode="w") as file:
    for i in range(len(top_movies)):
        file.write(f"{i + 1}) {top_movies[i]}\n")
        