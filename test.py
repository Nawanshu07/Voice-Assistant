# Inshorts News API Example
import requests

url = "https://github.com/cyberboysumanjay/Inshorts-News-API"
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url)
data = response.json()
print(data)
