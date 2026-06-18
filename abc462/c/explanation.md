# ABC462 C - Not Covered Points 解説

CodeQUEEN 2026 -qual- (AtCoder Beginner Contest 462) / 300点 / 2026-06-13 開催

公式問題: https://atcoder.jp/contests/abc462/tasks/abc462_c
公式エディトリアル: https://atcoder.jp/contests/abc462/editorial/21406

---

## 1. 問題

2次元平面に点 1..N があり、点 i の座標は (Xᵢ, Yᵢ)。
**X, Y はそれぞれ (1, 2, …, N) の順列**(同じ座標値は二度出ない)。

各 i について、左下を (0,0)、右上を (Xᵢ, Yᵢ) とする軸平行な長方形を考える。
その長方形の **内部(辺上は含まない)** に、N 個の点をどれも含まないような i の個数を求める。

- 制約: 1 ≤ N ≤ 3×10⁵
- 計算量目標: O(N log N) 程度(全探索 O(N²) は TLE)

---

## 2. 言い換え(コア)

点 j が「点 i の長方形の内部」に入る条件は、辺上を除くので

  **Xⱼ < Xᵢ かつ Yⱼ < Yᵢ**  (j は i の「真の左下」にいる)

したがって、

  点 i が条件を満たす(= Not Covered)
  ⇔ 自分より **左下にある点が 1 つも存在しない**

これは「左下フロンティア(下側の階段状の境界)に乗っている点」を数えることに等しい。

---

## 3. 解法 — X でソートして Y の最小値を累積更新

端から見たいので **X の昇順** に走査する。
X 昇順で見ると、「自分より左(Xが小)」の点はすべて走査済み。
その中に「自分より下(Yが小)」の点があるかどうかは、
**これまでに見た Y の最小値 minY** だけで判定できる。

- minY < Yᵢ なら、左下に点がある → Covered(数えない)
- Yᵢ < minY なら、左下に点がない → Not Covered(数える)、minY を更新

つまり「**X昇順に並べたときの Y の prefix minimum(左から見た最小値の更新回数)**」が答え。

計算量は ソート O(N log N) が支配的。

---

## 4. 擬似コード

```
読み込み: N, 点列 (X_i, Y_i)
点列を X の昇順にソート
minY = +∞
ans = 0
for (x, y) in sorted_points:
    if y < minY:
        ans += 1
        minY = y
print(ans)
```

---

## 5. 実装 (Python)

```python
import sys
input = sys.stdin.readline

N = int(input())
pts = [tuple(map(int, input().split())) for _ in range(N)]
pts.sort(key=lambda p: p[0])          # X 昇順

ans = 0
min_y = float("inf")
for _, y in pts:
    if y < min_y:
        ans += 1
        min_y = y
print(ans)
```

---

## 6. サンプルで確認

入力:
```
3
2 1
1 3
3 2
```
X昇順に並べ替え → (1,3), (2,1), (3,2)

| 順 | 点 (X,Y) | minY(直前) | y < minY? | 判定 | ans |
|----|----------|-----------|-----------|------|-----|
| 1 | (1, 3) | ∞ | yes | Not Covered | 1 |
| 2 | (2, 1) | 3 | yes | Not Covered | 2 |
| 3 | (3, 2) | 1 | no  | Covered | 2 |

出力: **2**(i=3 の長方形 (0,0)-(3,2) は内部に点1 (2,1) を含むので不適)。

---

## 7. 手書きメモ(memo.pdf)との対応

メモでは点 i が「覆われる」条件を **Xᵢ < Xⱼ ∧ Yᵢ < Yⱼ**(自分より右上に点がある)という
双対(右上フロンティア)の向きでも検討し、X を key にソートして二重ポインタで数える方針を描いている。
本質は同じ「ソートして片側の最小/最大を累積で持つ」=「階段(スタイ)フロンティアを数える」。
最終的には上記の **X昇順 × Yのprefix最小** で 1 パス O(N) に落ちるのが最短。

典型: ABC091 C - 2D Plane 2N Points などと同系統の「ソートして貪欲」。
