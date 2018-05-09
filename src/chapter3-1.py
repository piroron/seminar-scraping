import requests

# HTMLソースを得る
url = "http://www.shoeisha.co.jp/book/detail/9784798146072"
r = requests.get(url)
html = r.text
print(html)