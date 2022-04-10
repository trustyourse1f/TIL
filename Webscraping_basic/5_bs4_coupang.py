import requests
import re
from bs4 import BeautifulSoup

url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")

items=soup.find_all("li",attrs={"class":re.compile("^search-product")})
#print(items[0].find("div",attrs={"class":"name"}).get_text())

for item in items:
    name=item.find("div",attrs={"class":"name"}).get_text()
    price=item.find("strong",attrs={"class":"price-value"}).get_text()
    print(name,price)