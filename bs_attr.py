from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc, "html.parser")

sonuc = obj.find(id = "header")
sonuc = obj.find(class_= "baslik")
sonuc = obj.find(class_="bolum")
sonuc = obj.find_all(class_="bolum")[1]
sonuc = obj.select("#header")
sonuc = obj.select("#div1")
sonuc = obj.select(".bolum")
sonuc = obj.select(".bolum")[1]
sonuc = obj.select_one(".bolum")
sonuc = obj.div.attrs
sonuc = obj.h1.attrs["id"]
sonuc = obj.get_text(strip=True, separator=",")

#print(sonuc)

for a in obj.find_all("a"):
    #print(a.get("href"))
    print(a["href"])

