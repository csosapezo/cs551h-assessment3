import requests

a = "api-football-v1.p.rapidapi.com"
url = f"https://{a}/v3/fixtures"

querystring = {"id":"1094463"}

headers = {
	"X-RapidAPI-Key": "6ffe4e161dmshf6aed00c7147c2dp1f3149jsn5bbe4554bc4e",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())