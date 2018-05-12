### 今回使用する言語
**Python**を使います。
* [Pythonチュートリアル @fa[external-link gp-download]](https://docs.python.jp/3/tutorial/index.html)

+++

### 使用環境
マシンにダウンロードし、開発できる環境を一緒に作成します。

+++

@title[前提]
### よく使用するもの

* コマンドプロンプト
* PowerShell
* (Macの場合)ターミナル

資料上「コマンドライン」と呼びます。

+++

### ダウンロード
[Python ダウンロードサイト @fa[external-link gp-download]](https://www.python.org/downloads/release/python-365/)

`3.6.5`を選択。  
OSとエディションに合ったものをダウンロード→インストール

+++

@title[インストール時注意点]

### インストール時

* `for All Users`は、チェックを**外す**  
「仮想環境（後述）」を作るなら、チェックありでも支障はない
* `Add Python Path`には、チェックを**付ける**

+++?image=assets/pyinstall.PNG&size=auto 70%

+++

@title[起動確認]

### 起動確認
コマンドラインで、

```ps1
python --version
```

と入力。

```
Python 3.6.5
```

と表示されればOK

+++

@title[利用準備1]

* 仮想環境の作成

コマンドラインで、好きなパスに移動し、

```ps1
python -m venv [仮想環境名]
```

と入力し、仮想環境を作成する。  
（仮想環境名は何でもよい。myvenvとか）  

+++

@title[利用準備2]

* 仮想環境の起動

コマンドラインで、

```ps1
[仮想環境パス]\Scripts\Activate.ps1
```

と入力すると、仮想環境のPythonが起動する。  

* コマンドプロンプトの場合、`.bat`
* PowerShellの場合、`.ps1`
* Macターミナルの場合拡張子なし

+++

@title[利用準備3]

* pipのバージョンアップ  

コマンドラインで、

```ps1
python -m pip install --upgrade pip
```

と入力。（`pip`：モジュール管理ツール）

+++

@title[Jupyter Notebook1]
### エディタのインストール
以下のコマンドを入力

```ps1
pip install jupyter
```

+++

@title[Jupyter Notebook2]

### 起動

以下のコマンドを入力

```ps1
jupyter notebook
```

すると、ブラウザでノートが起動する。

続いて、ノートを作成する。

+++?image=assets/newnote.PNG&size=auto 70%

@title[Jupyter Notebook3]
