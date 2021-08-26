import json
import requests

url = "https://api.exchangerate.host/latest"

res = requests.get(url)

data = res.json()
# print(json.dumps(data, indent= 2))

rates={}


for rate in data["rates"]:
    price = data["rates"][rate]
    rates[rate] = price



# print(json.dumps(rates,indent=2))

print(50*rates["USD"]*rates["AED"])