# Splunk-CustomSearchCommand-FirstStep
[Splunk カスタムサーチコマンド (custom search command) 作成 ― はじめの一歩 ― - Qiita](https://qiita.com/msi/items/02d029d655e1f9285806) のサンプル

## 1. step1

[Splunk カスタムサーチコマンド (custom search command) 作成 ― はじめの一歩 ― - Qiita](https://qiita.com/msi/items/02d029d655e1f9285806) にて作成したファイル群。

* ディレクトリ `HelloWord-work/` に 引数を取らない `generatehello` を作成した。
* `HelloWorld-work/` を `$SPLUNK_HOME/etc/apps/HelloWorld/` としてコピーして利用する。

## 1-2. step1-2

[Splunk カスタムサーチコマンド (custom search command) 作成 その2 - Qiita](https://qiita.com/msi/items/ca5d3c553bd49d8665ac) にて作成したファイル群。

* イベントの個数を引数で指定できるようにした。
* 実行結果のイベントとして表示されるようにした。

## 2. step2

[Splunk のカスタムサーチコマンド作成 EventingCommand 編](https://qiita.com/msi/items/c41bbe35c806f487a482) にて作成したファイル群。

* 大文字に変換する toupper コマンドを作成した。
* Protocol Version 2 を利用。
* searchbnf.conf を設定することで、ヘルプを表示できるようにした。
