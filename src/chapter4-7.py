import requests
import lxml.html

# HTMLソースを得る
url = "http://www.shoeisha.co.jp/book/detail/9784798146072"
r = requests.get(url)
html = r.text

# HTMLをHtmlElementオブジェクトにする
root = lxml.html.fromstring(html)

path = "//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/p/a"

aTag = root.xpath(path)

for a in aTag:
    print(a.text)