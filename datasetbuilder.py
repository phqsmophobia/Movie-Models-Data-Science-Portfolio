from config import KEY,URL_START # always hide API KEY
import requests

#set up
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
refinedmovieselection = []

for entry in movieselection:
    url = f"{URL_START}/movie/{entry['id']}"
    refineresponse = requests.get(url, headers=header)
    if refineresponse.status_code == 200:
        refineddata = refineresponse.json()
        #collect what we need to make our first questions prediction
        refinedmovieselection.append({
            "title": refineddata["title"],
            "release_date": refineddata["release_date"],
            "genres": ", ".join(genre["name"] for genre in refineddata["genres"]),
            "budget": refineddata["budget"],
            "revenue": refineddata["revenue"],
        })
    else:
        #incase we fail to pull a movie's data
        print("could not retrieve the data for:", entry["id"], entry["title"])

# print each movie data
for entry in refinedmovieselection:
    print(entry)

# helps view the total movie count retrieved
print("count:", len(refinedmovieselection))