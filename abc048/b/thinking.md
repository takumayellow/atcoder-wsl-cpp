# abc048 B — Between a and b ...

- 問題: https://atcoder.jp/contests/abc048/tasks/abc048_b
- 提出（2026-08-04, Python）: [TLE](https://atcoder.jp/contests/abc048/submissions/78115809) → [WA](https://atcoder.jp/contests/abc048/submissions/78115968) → [AC](https://atcoder.jp/contests/abc048/submissions/78116111)
- 手書き原本: `Box/Photo Backup/手書き/atcoder/abc048/b/`（`20260925_174824.jpg`, `20260925_174819.jpg` の 2 枚）
- 再現: [thinking.pdf](thinking.pdf)（原本の再現。赤は後から入れた振り返り）

## つまずき

- **TLE**: $b \leq 10^{18}$ を見る前に、1 つずつ数えるループを書き始めた。
- **WA**: `b//x - a//x + 1` を提出した。$+1$ が正しいのは $a$ が $x$ で割り切れるときだけ。
  検算した 3 例のうち 2 例（`4 8 2`, `0 5 1`）がたまたま割り切れるケースで、
  3 例目（`1 100 3`）で「$+1$?」と迷ったのに確かめずに出した。

## 正しい考え方

$0$ 以上 $n$ 以下の $x$ の倍数の個数を $g(n) = \lfloor n/x \rfloor + 1$ とおくと、
$[a,b]$ の個数は $g(b) - g(a-1) = \lfloor b/x \rfloor - \lfloor (a-1)/x \rfloor$。
図（$a=4, b=8, x=2$ の数直線）は thinking.pdf の最後のページ。

$a=0$ のときは $\lfloor -1/x \rfloor = -1$（Python の `//` は負の方向へ切り捨て）なので、そのまま $0$ も数えられる。
C++ の `/` は $0$ 方向へ切り捨てるので `(a-1)/x` が $0$ になり、$a=0$ で 1 足りない。
C++ では `b/x - (a == 0 ? -1 : (a-1)/x)` のように分ける。

## 次に活かすこと

- 区間 $[a,b]$ の個数は、累積の差 $g(b) - g(a-1)$ で書く。端の $\pm 1$ を場合分けで直さない。
- 検算のサンプルに「端が条件を満たさないケース」を 1 つ入れる。迷った例は出す前に手で数える。
- 書き始める前に制約を見る。
