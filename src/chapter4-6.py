import requests
import lxml.html

# HTMLソースを得る
url = "http://www.shoeisha.co.jp/book/detail/9784798146072"
r = requests.get(url)
html = r.text

# HTMLをHtmlElementオブジェクトにする
root = lxml.html.fromstring(html)

paths = []

paths.append("//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/p/a[1]")
paths.append("//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/p/a[2]")
paths.append("//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/p/a[3]")

for path in paths:
    # XPathを指定して該当する要素のリストを得る
    author = root.xpath(path)
    # テキストを表示する
    print(author[0].text)
