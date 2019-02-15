# これは何? #

HTMLの一部をキーワードリストを元にハイライトします。


## 環境 ##

ターミナルで`python3`のバージョンを確認してください。

```sh
python3 --version
Python 3.7.2
```

上記は作者の環境を表示したものですが、標準のライブラリしか使っていないので、`python3`なら動くと思います。

つまり

```sh
python --version
```

を実行して`Python 3.*`なら多分大丈夫です。

ここまで確認できたら適当な場所に`cd`して`git clone`してください。

例として`$HOME/Works/highlight`にクローンするなら下記のような手順になるかと思います。

```sh
$ cd "$HOME"
$ mkdir -p "$HOME"/Works
$ cd "$HOME"/Works
$ git clone https://github.com/ShinNakamura/highlight.git highlight
$ cd ./highlight
```


## Usage ##

必要なものをまとめると、

* `highlight.py` このファイルが実行ファイルです。Pythonで書かれています。

* `t.out.html` このファイルが最終的に結果をHTMLで吐くためのテンプレートになります。

* ハイライトしたい元ファイルが必要です。テスト用に`filesForTest/src.txt`を用意しました。

* ハイライトしたいキーワードを改行区切りで記載したファイルが必要です。テスト用に`filesForTest/kws.txt`を用意しました。

以上を組み合わせて下記のようにコマンドを組み立てて実行してください。

```sh
python3 highlight.py t.out.html filesForTest/src.txt filesForTest/kws.txt >result.html
```

上記のサンプルの場合は、`result.html`に結果が出力されます。

この結果HTMLをブラウザにドラッグ・アンド・ドロップなどすると、ハイライトした状態を確認できます。

ハイライト後のサンプルは[こちら](https://screenshots.firefox.com/mxojoI19ozwuC8HN/null)
