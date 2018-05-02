### スクレイピングとは
Webにある情報を、抽出すること。  

+++?image=assets/scraping.PNG

@title[スクレイピング]

![scraping](assets/scraping.png)

+++

### 前提知識

ブラウザで表示されている情報の正体を見る

<ul>
<li class="fragment">ブラウザで、適当なページを表示する</li>
<li class="fragment">右クリック - ソースの表示 等</li>
</ul>

+++?image=assets/viewsource.PNG

@title[ソースの表示]

+++

@title[詳細]

### ブラウザの役割
ソースに基づいて、表示している。  
この記述言語を`HTML`という。

```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
</html>
```