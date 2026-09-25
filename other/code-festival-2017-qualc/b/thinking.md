# code_festival_2017_qualc B — Similar Arrays

- 問題: https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_b
- 提出（2026-08-04, Python）: [AC](https://atcoder.jp/contests/code-festival-2017-qualc/submissions/78112999)（1 回目で AC）
- 手書き原本: `Box/Photo Backup/手書き/atcoder/code_festival_2017_qualc/b/`（`20260925_174806.jpg` の 1 枚。撮影 2026-09-25）
- 再現: [thinking.pdf](thinking.pdf)（原本の再現。赤は後から入れた振り返り）

## つまずき

無し。「$\exists$（どれか 1 つが偶数）」を直接数えずに、余事象の「$\forall$（全部奇数）」に切り替えたのが効いた。

## 正しい考え方

1. 条件 $|x_i - y_i| \leq 1$ を $-1 \leq x_i - y_i \leq 1$、つまり $y_i = x_i + \lbrace 0, \pm 1 \rbrace$ の 3 通りと書き直す。
2. 「積が偶数 $\iff$ どれかの項が偶数」なので、余事象「全部奇数」を数える。
3. 全体は各項 3 通りで $3^n$。全部奇数になるのは、$A_i$ が偶数の項（個数 $m$）だけ 2 通り（$\pm 1$）、奇数の項は 1 通り（そのまま）なので $2^m$。
4. 答えは $3^n - 2^m$。サンプルで検算: `2 / 2 3` は $m=1$ で $3^2 - 2^1 = 7$、`3 / 3 3 3` は $m=0$ で $3^3 - 2^0 = 26$。

例 $A = (2, 3)$ で数えた図は thinking.pdf の最後のページ。

## 次に活かすこと

- 「少なくとも 1 つ〜」を数える問題は、まず余事象「全部〜でない」が積で書けないかを見る。
- 検算で $m = 0$ の端（全部奇数）も確かめていたのはよかった。
