import  requests
r=requests.get("http://google.com")
r.raise_for_status()
#print(r.text)
with open("data.html","w",encoding="UTF-8") as f:
    f.write(r.text)