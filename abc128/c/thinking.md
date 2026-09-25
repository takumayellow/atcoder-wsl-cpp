# abc128 C - Switches

- 問題: https://atcoder.jp/contests/abc128/tasks/abc128_c
- 手書き原本: `Box/Photo Backup/手書き/atcoder/abc128/c/`（20260925_174812.jpg、撮影 2026-09-25）
- 提出: 2026-08-06 [CE](https://atcoder.jp/contests/abc128/submissions/78154478)（C++ のコードを Python で提出）→ [AC](https://atcoder.jp/contests/abc128/submissions/78154485)（C++23）
- 清書: [explanation.md](explanation.md)

## メモで考えたこと

1. N 個のスイッチ・M 個の電球、電球 i は k_i 個のスイッチ s_{i1} … s_{ik_i} につながる、と整理した。
2. 点灯条件を「(s_{i1}, …, s_{ik_i} のうち on の個数) % 2 == p_i」と式にした。
3. 入力形式を書き写し、サンプル `2 2 / 2 1 2 / 1 2 / 0 1` で「電球 1 はスイッチ 1, 2 のうち偶数個 on、電球 2 はスイッチ 2 が奇数個 on」と読んで、条件を満たす組を手で探した。

メモは問題の読み取りまでで、解法（全探索）はメモに書いていない。

## つまずき

- **CE**: C++ のコードを言語 Python のまま提出した（同じ分に C++23 で出し直して AC）。
- 解法の根拠（N ≤ 10 だから 2ᴺ ≤ 1024 通りを全部試せる）がメモに無い。

## 正しい考え方

スイッチの on/off を N ビットの整数 bit で表し、bit = 0 … 2ᴺ−1 を全部試す。各電球について on のスイッチ数の偶奇が p_i と一致するかを見る。O(2ᴺ · Σk_i)。
詳しくは [explanation.md](explanation.md)。

## 次に活かすこと

- メモに問題を書き写したら、**制約を見て計算量の方針を 1 行書く**（ここでは「N ≤ 10 → bit 全探索」）。
- 提出前に言語の選択を確認する（`acsub` を使えば拡張子から自動で決まる）。
