import requests, json

url = "https://climate-news-feed.p.rapidapi.com/page/1"

querystring = {"limit":"4"}

headers = {
	"x-rapidapi-key": "e90951f38fmsh4139c9a69870b33p10dc08jsn2be5f0bd4413",
	"x-rapidapi-host": "climate-news-feed.p.rapidapi.com"
}
response=requests.get(url, headers=headers, params=querystring)
with open("news.json", "w") as file:
    json.dump(json.loads(response.text), file, indent=4)
    file.close()
