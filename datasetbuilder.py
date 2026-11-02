from config import KEY,URL_START
import requests

url = f"{URL_START}/movie/popular"

header = {"Authorization": f"Bearer {KEY}","accept":"application/json"}

movieselection = []

for i in range(1,26):
    response = requests.get(url, headers=header, params={"page": i})
    if response.status_code == 200:
        data = response.json()
        movieselection.extend(data["results"])
    else:
        print("connection failed :(")
        print(response.text)

for entry in movieselection:
    print(entry)