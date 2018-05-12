@title[PowerShellを使えるようにする]

### 管理者権限で起動

[このサイト](http://www.atmarkit.co.jp/ait/articles/0805/16/news139.html)を参考に、  
実行権限を与えます。

+++

@tiitle[起動]

```ps1
[仮想環境パス]\Scripts\Activate.ps1
```

例：

```ps1
cd c:\seminar
.\myvenv\Scripts\Activate.ps1
```

+++

@title[スクリプトでJupyter起動]

### スクリプトで起動

gitHubの

`src\scripts\execute_jupyter.ps1`

の中身を、自分自身のパスに変更し、

ファイルを右クリック - PowerShellで実行

とします。