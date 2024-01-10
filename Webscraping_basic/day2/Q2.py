import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/sise_rise.naver"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
data=soup.select("td")

print("종목             |             현재가")
for i in data:
    if i.a:
       print(i.a.text,":",i.next_sibling.next_sibling.text)
