import requests
import lxml.html

# HTMLソースを得る
url = "http://www.shoeisha.co.jp/book/detail/9784798146072"
r = requests.get(url)
html = r.text

# HTMLをHtmlElementオブジェクトにする
root = lxml.html.fromstring(html)

# XPathを指定して該当する要素のリストを得る
titleH1 = root.xpath("//*[@id=\"cx_contents_block\"]/div/section/h1")

# リストの1番目のテキストを表示する
print(titleH1[0].text)