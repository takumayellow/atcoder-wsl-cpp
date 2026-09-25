# code_festival_2017_qualc B - Similar Arrays

- 問題: https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_b
- 手書き原本: `Box/Photo Backup/手書き/atcoder/code_festival_2017_qualc/b/`（20260925_174806.jpg、撮影 2026-09-25）
- 提出: 2026-08-04 Python [AC](https://atcoder.jp/contests/code-festival-2017-qualc/submissions/78112999)（1 回目で AC）

## メモで考えたこと

1. 条件 |x_i − y_i| ≤ 1 を −1 ≤ x_i − y_i ≤ 1、つまり y_i = x_i + {0, ±1} の 3 通りと書き直した。
2. 「積が偶数 ⇔ ∃ 偶数の項」なので、**余事象「全部奇数」** を数えることにした。
3. 全体は各項 3 通りで 3ⁿ。全部奇数になるのは、A_i が偶数の項（個数 m）だけ 2 通り（±1）、奇数の項は 1 通り（そのまま）なので 2ᵐ。
4. 答えは 3ⁿ − 2ᵐ。サンプルで検算: `2 / 2 3` は m = 1 で 3² − 2¹ = 7、`3 / 3 3 3` は m = 0 で 3³ − 2⁰ = 26。

## つまずき

無し。「∃（どれか 1 つ）」を直接数えずに、余事象の「∀（全部）」に切り替えたのが効いた。

## 次に活かすこと

- 「少なくとも 1 つ〜」を数える問題は、まず余事象「全部〜でない」が積で書けないかを見る。
- 検算で m = 0 の端（全部奇数）も確かめていたのはよかった。
