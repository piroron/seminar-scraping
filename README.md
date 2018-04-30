# seminar-scraping
勉強会向けスライド

スクレイピングの勉強会、というより、スクレイピングを題材にしたプログラミング勉強会

## 勉強会使用環境
クライアントに構築する。

## 記法メモ

`---`

横ページ

`+++`

縦ページ

## 内容

サンプルの再現

サンプルの拡張

## 画像の設定
GitHubのマークダウンに則り、先頭はスラッシュにする。

## pullしないとできないこと
* コードのハイライト（@[2]みたいなの）
* `@title[Some custom label]`のような、Table of Contents
* フラグメント：1行ずつアニメーション（文末に、各行で位置を揃えて「|」）
* リンクにつける画像
* 別のマークダウン表示

## 別のマークダウンを表示

イメージと同じように、リンク的な機能がある。  
モジュール化をイメージすると分かりやすい気がする。

[リンク：Modular Markdown](https://github.com/gitpitch/gitpitch/wiki/Modular-Markdown)

[リンク：Asset Sharing](https://github.com/gitpitch/gitpitch/wiki/Asset-Sharing)

* フォルダを作り、そこに任意のマークダウンを置く
* サブスライドのネストはできない模様

## 注釈
ページ末尾に

```
Note:
注釈内容
```

のように記述する。

`Speaker Mode`の際、自分に見える画面に、そのページの注釈が表示される。

## サブディレクトリのスライドを表示

**サブスライドの使用を前提とする。**

基本は、

`https://gitpitch.com/[user]/[repo]/[branch]`

の規則に則り記載されたURLしか受け付けず、リポジトリのルートにある`PITCHME.md`を表示する。

しかし、特定のトピック（Tipsとか）のみを記載したスライドを別途作成したい、という場合がある。

その場合、サブディレクトリに、別の`PITCHME.md`を配置し、以下の構文で呼ぶ。

`https://gitpitch.com/[user]/[repo]/[branch]?p=[subdirectory-path]`

`[subdirectory-path]`は、ルートからの相対パス。フォルダ区切りは`/`で良い。

なお、サブディレクトリのスライドで、サブスライドを参照する場合、  
サブスライドへのパスは**ルートからの相対**で記述する。  
