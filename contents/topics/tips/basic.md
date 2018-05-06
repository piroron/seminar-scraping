@title[下準備]

### モジュールのインストール
`pip`で、以下のモジュールを取得する。

* Requests

```
pip install requests
```

+++

@title[Webページ取得]

### ページへのアクセス

```python
import requests

# HTMLソースを得る
url = "http://www.shoeisha.co.jp/book/detail/9784798146072"
r = requests.get(url)
html = r.text
```
@[1](requestsというモジュールを使えるようにする)
@[4](アクセスするページのURLを指定)
@[5](webページを取得（getリクエスト）)
@[6](textで、webページのHTMLを取得できる)

+++

@title[HTMLの構成]

### HTMLの解説

HyperText Markup Language の略。  
簡単に言うと、「Webの共通言語」。  
（マークアップ言語とは、形式言語のこと）

階層構造になっている。  

```html
<html lang="ja">
    <body>
        <p>
            <h1>Hello World!</h1>
            ようこそ世界！
        </p>
    </body>
</html>
```

+++

@title[HTMLへのアクセス]

### 扱い
文字列として扱うと、プログラムで扱うのは大変。

アクセスを簡単にする方法は用意されている。

<ul>
<li class="fragment">XPath</li>
<li class="fragment">CSSセレクター</li>
</ul>

+++

@title[HTML構造]

### 構造
例えば、リンクを示す要素。

```html
<a 
    href="/book/detail/9784798155098">
    Webサイトパフォーマンス実践入門  高速なWebページを作りたいあなたに
</a>
```
@[1-2](開始タグ。この場合、「aタグ」と呼ぶ)
@[2](属性。hrefは、リンク先を指定する)
@[3](タグの中身。この場合、リンクのテキストを指す)
@[4](終了タグ。必ず「/タグ名」で記述する)