import requests
import lxml.html

# HTMLソースを得る
r = requests.get("http://www.shoeisha.co.jp/book/detail/9784798146072")
html = r.text

# HTMLをHtmlElementオブジェクトにする
root = lxml.html.fromstring(html)

# XPathを指定して該当する要素のリストを得る
author1 = root.xpath("//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/p/a[1]")
author2 = root.xpath("//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/p/a[2]")
author3 = root.xpath("//*[@id=\"cx_contents_block\"]/div/section/div/div[2]/p/a[3]")

# リストの1番目のテキストを表示する
print(author1[0].text)
print(author2[0].text)
print(author3[0].text)
