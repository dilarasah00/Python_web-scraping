from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc, "html.parser")

sonuc = obj.div
sonuc = obj.find('div')
sonuc = obj.find_all('div')[1]
sonuc = obj.find_all('div')[1].ul.find_all('li')[1]
sonuc = len(obj.find_all('div'))

#print(sonuc)

divs = obj.find_all('div')

for div in divs:
    if div.h2.a != None:
        print(div.h2.a.string.strip())
    else:
        print(div.h2.string.strip())

for a in obj.find_all('a'):
    print(a)

