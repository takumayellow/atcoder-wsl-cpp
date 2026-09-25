# abc473 C — Change Schools

- 問題: https://atcoder.jp/contests/abc473/tasks/abc473_c
- 提出（2026-08-29, Python）: [WA](https://atcoder.jp/contests/abc473/submissions/78822723) → [AC](https://atcoder.jp/contests/abc473/submissions/78825493)
- 手書き原本: `Box/Photo Backup/手書き/atcoder/abc473/c/`（`20260925_174830.jpg` の 1 枚。撮影 2026-09-25）
- 再現: [thinking.pdf](thinking.pdf)（原本の再現。赤は後から入れた振り返り）

## メモで考えたこと

メモでは、クラスを袋として描いて「K class / N 人」「人数 max のクラス」「count」を置き、
高橋くんが入るとそのクラスが $+1$ になることを書いた。そのうえで「class num sort $\to$ top, next ...」と並べ、
「top, top $-1$ の個数」と結論を書いた。この結論（人数が max か max $-1$ のクラスの数）は正しい。

## つまずき

- **WA**: コードでは「top $-1$」を **「2 番目に大きい人数」** として数えていた（`b[-2]`）。
  2 番目に大きい人数が max $-1$ より小さいとき、そのクラスに入っても max のクラスに負けるので数えてはいけない。
  メモの「top $-1$」は値としての max $-1$ なのに、コードで「順位としての 2 番目」に読み替えてしまった。
- **AC 版にも潜在的なバグがある**: `b = list(set(a))` はソートされる保証がない。
  小さい整数ではたまたま昇順に並ぶが、`list(set([1, 8]))` は `[8, 1]` になる。
  実際に `10 3 / 1 1 1 1 1 1 1 1 2 3`（人数 8, 1, 1）を AC 版に入れると **2** を出す（正しくは 1）。
  テストケースにこの形が無かったので通っただけ。

## 正しい考え方

各クラスの人数を $c_i$、$M = \max c_i$ とする。クラス $i$ に入ると $c_i + 1$ になり、ほかのクラスは最大 $M$ のまま。
喜ぶ条件は $c_i + 1 \geq M$、つまり $\boldsymbol{c_i \geq M - 1}$。これを満たすクラスを数えるだけでよい（ソートも set も要らない）。

図は thinking.pdf の最後のページ。

```python
n, k = map(int, input().split())
c = [0] * k
for x in map(int, input().split()):
    c[x - 1] += 1
m = max(c)
print(sum(1 for v in c if v >= m - 1))
```

## 次に活かすこと

- メモの結論を **条件式（ $c_i \geq M - 1$ ）** の形で書いてからコードにする。
  「top $-1$ の個数」のような言葉のままだと、コードで別の意味に化ける。
- 並び順が欲しいときは `sorted(set(a))`。`set` の順序に頼らない。
