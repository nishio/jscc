============================
 日本語でのカジュアルなメモ
============================

- watch周り

  - Windows(cygwin)だとwatchmedoがうまく動かないらしい

  - 現状watchしているプロセスを殺す方法がない

  - →いっそPythonでファイルの更新日時をポーリングするののほうがよい？


- クライアントツール

  - Makefileとbuild.shとclient.pyをカレントディレクトリにコピーする設計になっているけど、
    　そもそもプロジェクトの内容に応じて書き換える必要があるのはMakefileだけだから
    　残りの2つはjscc/client/に置きっぱなしでいいんじゃない？
    　compile.logとlint.logもjsccの中に作ったほうがいいんじゃない？なるべく汚さない方針で。

    - 既存プロジェクトに追加する場合、.jsccを作ってその中に入れたらいいのでは
    - 新規プロジェクトの作成も同様に。

  - growlnotifyは必須ではないので(僕は使うけど)インストールされてるかどうか判断して使うようにしたいがどう書く？

  - 将来的に複数のプロジェクトで複数人で使う際には識別のためにプロジェクト名とユーザ名を送る必要がある。
    　今は一人で使う想定でシングルユーザ・シングルプロジェクト



- 可視化サーバ

  - 将来的に複数のプロジェクトと複数人で使う場合にはトップページはプロジェクト一覧にして /project_name/nishio/ みたいなURLで見るようにする

  - いま過去の履歴を保存していない。sqliteかなんかで保存しておく。最新n件を取るAPIが必要。

  - 今はJSで1秒1回サーバにポーリングしているが、タイムアウトしてないせいでサーバが止まっているとリクエストが溜まってしまう？
