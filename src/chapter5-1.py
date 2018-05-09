import requests
import lxml.html

# HTMLソースを得る
url = "http://www.shoeisha.co.jp/book/detail/9784798146072"
r = requests.get(url)
html = r.text

# HTMLをHtmlElementオブジェクトにする
root = lxml.html.fromstring(html)

path = "//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/dl/dd"

dds = root.xpath(path)

for dd in dds:
    # print(type(dd.attrib))
    for k, v in dd.attrib.items():
        print(k)
        print(v)
    # 書籍情報を取得する
    item_prop = dd.attrib.get("itemprop")
    
    if item_prop == "datePublished":
        print("publishDate：" + dd.text)
    elif item_prop == "isbn":
        print("isbn：" + dd.text)
    elif item_prop == "offers":
        # 金額を取得
        pass
