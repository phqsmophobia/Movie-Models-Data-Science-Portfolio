from config import KEY,URL_START
import requests

url = f"{URL_START}/movie/popular"

header = {"Authorization": f"Bearer {KEY}","accept":"application/json"}

movieselection = []

# obtain the default data for 500 movies 
# (page 1-26 to do first 25 pages as TMDB stores entries in pages 
# of 20 entries as 25x20=500)
for i in range(1,26):
    response = requests.get(url, headers=header, params={"page": i})
    if response.status_code == 200:
        data = response.json()
        movieselection.extend(data["results"])
    else:
        print("connection failed :(")
        print(response.text)

# refine our movie data