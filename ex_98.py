import requests
import pandas as pd 

url = 'https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks'
response = requests.get(url)

if response.status_code == 200:
    # Access the response content as a JSON object (Python dictionary)
    json_data = response.json()
    print(json_data)
else:
    print(f"Request failed with status code: {response.status_code}")
