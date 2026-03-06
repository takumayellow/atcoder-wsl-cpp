# tessoku-book

AtCoder `tessoku-book` のローカル解答集です。`contest.acc.json` にある 151 問が `a/`, `b/`, `c/` 配下に入っています。

## 収録状況

- 公式問題一覧: <https://atcoder.jp/contests/tessoku-book/tasks>
- ローカル収録数: 151
- `contest.acc.json` の定義と問題ディレクトリは一致

## 実行方法

この環境では Homebrew GCC 15 と Xcode SDK を組み合わせると `main.cpp` を実行できます。

```sh
scripts/run_cpp.sh a/a01 a/a01/test/sample-1.in
```

サンプルまとめて検証:

```sh
scripts/test_samples.sh a/a01
```

問題文を CLI で表示:

```sh
scripts/problem_statement.sh A06
```

問題文を TeX に書き出す:

```sh
scripts/export_problem_tex.sh A06
```

単体 PDF を作る:

```sh
scripts/build_problem_pdf.sh A06
```

解答 `main.cpp` がテンプレートでなければ、同じ PDF の末尾に自動で載ります。

## PDF ビルド

LaTeX の中間生成物を消して PDF だけ残す:

```sh
make pdf
```

生成先:

```sh
build/main.pdf
```

PDF も含めて消す:

```sh
make distclean
```

## 補足

- `#include <bits/stdc++.h>` と `#include <atcoder/all>` を使う前提です。
- ACL は `/Users/uenoyuuta/atcoder-wsl-cpp/ac-library` を参照します。
