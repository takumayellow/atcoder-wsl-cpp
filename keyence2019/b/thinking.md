# keyence2019 B — KEYENCE String

- 問題: https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b
- 提出（2026-08-04, Python）: [AC](https://atcoder.jp/contests/keyence2019/submissions/78117551)（1 回目で AC）
- 手書き原本: `Box/Photo Backup/手書き/atcoder/keyence2019/b/`（`20260925_174816.jpg` の 1 枚。撮影 2026-09-25）
- 再現: [thinking.pdf](thinking.pdf)（原本の再現。赤は後から入れた振り返り）

## つまずき

- **メモ**: 取り除く区間（○）が keyence のどこに入るかを並べ、「前半 + 後半に分ける位置は 8 通りしかない」形まで見えていた。
  ただし書いた分け目は 5 つで、$k=0$（先頭を取る）・$k=4$・$k=7$（末尾を取る）が無い。
- **提出**: メモの「分け方 8 通り」ではなく、取り除く区間 $[i,j)$ を $O(N^2)$ 通り全部試した（$N \leq 100$ なので間に合う）。
  ループが `for j in range(i, l)` で $j = l$ を試さないため、末尾を取り除く形が抜けている。
  `keyencex` や `keyenceabc` で `NO` を出す（正しくは `YES`）。実際に動かして確かめた。
  テストケースにこの形が無く AC になった。`range(i, l + 1)` にすれば通る。

## 正しい考え方

$k = 0, \dots, 7$ について、$S$ が `keyence[:k]` で始まり `keyence[k:]` で終わるかを見る。$O(8N)$。
図は thinking.pdf の最後のページ。

```python
s = input()
t = "keyence"
print("YES" if any(s.startswith(t[:k]) and s.endswith(t[k:]) for k in range(8)) else "NO")
```

## 次に活かすこと

- メモで見つけた「分け方の数が小さい」という構造は、そのまま計算量の削減に使える。
  制約が小さくて全探索で通るときも、メモの発想をコードに移せるかを一度考える。
- 分け目を並べるときは、両端（$k=0$ と $k=7$）を最初に書く。
- 区間 $[i,j)$ を全部試すときは、`range` の終わりが「空の区間」「末尾まで」を含むか確かめ、端の入力（`keyencex`）で試してから出す。
