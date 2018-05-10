import requests
import lxml.html

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

with open("result.txt", "w", encoding="utf-8") as f:
    for prop in pub:
        # 書籍情報を取得する
        item_prop = prop.attrib.get("itemprop")

        if item_prop == "datePublished":
            f.write("publishDate：" + prop.text + "\n")
        elif item_prop == "isbn":
            f.write("isbn：" + prop.text + "\n")
        elif item_prop == "price":
            f.write("price：" + prop.text + "\n")
        elif item_prop == "numberOfPages":
            f.write("pages：" + prop.text + "\n")