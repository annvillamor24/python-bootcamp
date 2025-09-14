import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")
data = response.json()
# Get the latest conversion rate from USD to PHP
# print(response.json())
print (data["rates"] ["PHP"])
