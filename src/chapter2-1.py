import requests
import lxml.html

# HTMLソースを得る
url = "http://www.shoeisha.co.jp/book/detail/9784798146072"
r = requests.get(url)
html = r.text

# HTMLをHtmlElementオブジェクトにする
root = lxml.html.fromstring(html)

x1 = "//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/p/a[1]"
x2 = "//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/p/a[2]"
x3 = "//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/p/a[3]"

# XPathを指定して該当する要素のリストを得る
author1 = root.xpath(x1)
author2 = root.xpath(x2)
author3 = root.xpath(x3)

# リストの1番目のテキストを表示する
print(author1[0].text)
print(author2[0].text)
print(author3[0].text)
