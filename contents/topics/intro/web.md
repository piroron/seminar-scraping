@title[Web基礎]

### Webページ

ブラウザで表示されているページの正体を見る

<ul>
<li class="fragment">ブラウザで、適当なページを表示する</li>
<li class="fragment">右クリック - ソースの表示 等</li>
</ul>

+++?image=assets/viewsource.PNG&size=auto 90%

@title[ソースの表示]

+++

@title[ブラウザとは]

### ブラウザの役割
文字列のソースに基づいて、表示している。  
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

+++

@title[Web技術の基本]

普段見ているWebページは、

<ul>
<li class="fragment">URLを指定して、リクエストを投げる</li>
<li class="fragment">レスポンスが**文字列(html)**で返ってくる</li>
<li class="fragment">ブラウザが中身を解釈して表示</li>
</ul>