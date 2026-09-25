# keyence2019 B - KEYENCE String

- 問題: https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b
- 手書き原本: `Box/Photo Backup/手書き/atcoder/keyence2019/b/`（20260925_174816.jpg、撮影 2026-09-25）
- 提出: 2026-08-04 Python [AC](https://atcoder.jp/contests/keyence2019/submissions/78117551)（1 回目で AC）

## メモで考えたこと

1. 「連続する部分文字列を 1 か所だけ取り除いて keyence にできるか」を、keyence のどこに取り除く区間（○）が入るかで並べた。
   - ○keyence○（先頭か末尾）、○k○eyence○、○keyen○ce○、○keyenc○e○、○ke○yence○ …
2. keyence を「前半 + 後半」に分ける位置は 8 通りしかない、という形が見えている。

## つまずき

無し。ただし提出コードはメモの「分け方 8 通り」ではなく、取り除く区間 [i, j) を O(N²) 通り全部試している（N ≤ 100 なので間に合う）。

## 正しい考え方

k = 0 … 7 について、S が keyence[:k] で始まり keyence[k:] で終わるかを見る。O(8·N)。

```python
s = input()
t = "keyence"
print("YES" if any(s.startswith(t[:k]) and s.endswith(t[k:]) for k in range(8)) else "NO")
```

## 次に活かすこと

- メモで見つけた「分け方の数が小さい」という構造は、そのまま計算量の削減に使える。制約が小さくて全探索で通るときも、メモの発想をコードに移せるかを一度考える。
