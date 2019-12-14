import requests
import json

file=open("js.json","a")
shearch = input("type request:")

data = requests.get("https://api.github.com/search/repositories?q=" + shearch)
data = json.loads(data.content)

for l in data["items"]:
    if l['private'] == False:
        a={l["full_name"],l['private']}
        file.write( )
        print(a)
        file.close()
