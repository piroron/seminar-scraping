import requests
import lxml.html
import json

# HTMLソースを得る
url = "http://www.shoeisha.co.jp/book/detail/9784798146072"
r = requests.get(url)
html = r.text

# HTMLをHtmlElementオブジェクトにする
root = lxml.html.fromstring(html)

path = "//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/dl"
dl = root.xpath(path)
relation_path = ".//*[@itemprop]"
pub = dl[0].xpath(relation_path)

books = [] # list
book = {} # dict

for prop in pub:
    # 書籍情報を取得する
    book[prop.attrib.get("itemprop")] = prop.text

books.append(book)

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(books, f, ensure_ascii=False, indent=2)