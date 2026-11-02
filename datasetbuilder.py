from config import KEY,URL_START
import requests

connecturl = f"{URL_START}/movie/popular"

header = {"Authorization": f"Bearer {KEY}","accept":"application/json"}

response = requests.get(connecturl, headers=header)

if response.status_code == 200:
    print("connection made!")
else:
    print("connection failed :(")
    print(response.text)