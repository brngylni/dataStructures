import requests
import json

class MovieDb:
    def __init__(self):
        self.apiUrl = "https://api.themoviedb.org/3/"
        self.apiKey = "c9f89b7c73965fea70e6a536e875600e"

    def getPopulars(self):
        response = requests.get(f"{self.apiUrl}movie/popular?api_key={self.apiKey}&language=en-us&page=1")
        return response.json()
    def search(self, query):
        response = requests.get(f"{self.apiUrl}search/keyword?api_key={self.apiKey}&query={query}&page=1")
        return response.json()
movieApi = MovieDb()

while True:
    select = input("1- Popular Movies\n2- Search\n3- Exit\nSelection : ")

    if(select=="3"):
        break
    else:
        if(select == "1"):
            result = movieApi.getPopulars()
            for movie in result["results"]:
                information = f" Name : {movie['original_title']} && Release Date : {movie['release_date']}"
                print(information)
        elif(select == "2"):
            query = input("Please enter what you want to search : ")
            result = movieApi.search(query)
            for query in result["results"]:
                print("Name : "+query["name"])


