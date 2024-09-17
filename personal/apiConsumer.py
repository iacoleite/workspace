import random

import requests

api_url = "https://catfact.ninja/breeds"
response = requests.get(api_url)
responseData = response.json().get("data")

totale = response.json().get("total")


print(response.json())
print(totale)
ind = random.randint(1,int(totale))
pag = 1
if (ind > 25 and ind <=50):
    pag = 2
elif (ind > 51 and ind <=75):
    pag = 3
elif (ind > 75 and ind <= totale):
    pag = 4

api_update = api_url + f"?page={pag}"
newResponse = requests.get(api_update)
if (ind > 25):
    ind = ind%25
print(newResponse.json().get("data")[ind].get("breed"))



# https://catfact.ninja/breeds?page=4

