import requests
import pandas as pd 

url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=t3gW84nq0nMOreLLBmaM4AdgIWQx1YFO"
response = requests.get(url)

if response.status_code == 200:
    # Access the response content as a JSON object (Python dictionary)
    json_data = response.json()
    print(json_data)
else:
    print(f"Request failed with status code: {response.status_code}")
