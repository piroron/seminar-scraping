## なぜPythonだったのか

<ul>
<li class="fragment">他の言語に比べて、比較的簡単</li>
<li class="fragment">実行に手間がかからない</li>
<li class="fragment">機械学習等で流行っている</li>
</ul>

+++

### 別の言語

* 「C#」という言語の場合


C#：マイクロソフトが作っている言語

+++

@title[C#]

```cs
using static System.Console;

public class Hello {
    public static void Main() {
        int value = int.Parse(ReadLine());
        int pay_amount = 0;
        WriteLine("残り所持金" + value.ToString() + "円。");
        if (value >= 120) {
            WriteLine("ジュース買っちゃえ！");
            pay_amount = 120;
        } else if (value >= 100) {
            WriteLine("水を買う！");
            pay_amount = 100;
        } else {
            WriteLine("何も買えない！");
        }
        if (pay_amount != 0) {
            int rest = value - pay_amount;
            WriteLine("残り所持金" + rest.ToString() + "円。");
            if (rest == 0) {
                WriteLine("お金がない！");
            }
        }
    }
}
```

Note:
なんで言語によって書き方が違うのか、と言って、次のスライド

---

@title[compiler]

![compiler](assets/compile.png)

---

@title[compiler2]

![compiler](assets/compile2.png)

Note:
機械語に近い言語ほど、高速に動作しやすい。  
ただし、人間が読むのは難しくなる

結局、システムを作るのは人間なので、読みやすいほうがいい  
作りやすさ、読みやすさが様々あったため、多くの言語が生まれた

なお、腕試しに言語（とコンパイラ）を作る人もいる。

---

@title[言語選定]

### どの言語が良いのか

<ul>
<li class="fragment">どの言語にも、得意不得意はある</li>
<li class="fragment">勉強目的なら、慣れるまでは一つに絞ったほうがいい</li>
<li class="fragment">事業目的なら、用途に応じて決める</li>
</ul>

+++

@title[言語選定例]

### 主観による言語選定

|用途|言語|理由等|
|---|---|---|
|ゲーム|C#|Unityとの親和性|
|機械学習|Python|ライブラリが充実|
|組み込み（Iot）|C言語|CPUと親和性が高い|
|業務系|Java、C#|WindowsならC#が楽|

+++

@title[Web系]

### Webは？

<ul>
<li class="fragment">必須</li>
    <ul>
    <li class="fragment">JavaScript</li>
    <li class="fragment">CSS</li>
    </ul>
<li class="fragment">その他（どれか使う）</li>
    <ul>
    <li class="fragment">Ruby(Rails)</li>
    <li class="fragment">Python(Django,Flask)</li>
    <li class="fragment">Java(Play, Spring Framework)</li>
    <li class="fragment">C#(ASP.NET MVC)</li>
    </ul>
</ul>