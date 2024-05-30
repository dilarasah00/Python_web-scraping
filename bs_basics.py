from bs4 import BeautifulSoup

with open("index.html") as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc, "html.parser")

sonuc = obj.title.string
sonuc = obj.body.h1
sonuc= obj.h1.string
sonuc = obj.ul.li

print(sonuc)