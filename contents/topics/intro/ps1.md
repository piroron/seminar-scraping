@title[PowerShellを使えるようにする]

### 管理者権限で起動

[このサイト](http://www.atmarkit.co.jp/ait/articles/0805/16/news139.html)を参考に、  
実行権限を与えます。

+++

@title[起動]

* PowerShellでPython起動

下記パスは、自身の環境に合わせてください。

```ps1
cd c:\seminar
.\myvenv\Scripts\Activate.ps1
```
@[1](Jupyter等があるパスに移動)
@[2](仮想環境をアクティブにする)

+++

@title[スクリプトでJupyter起動]

### スクリプトで起動

gitHubの

`src\scripts\execute_jupyter.ps1`

の中身を、自分自身のパスに変更し、

ファイルを右クリック - PowerShellで実行

とします。