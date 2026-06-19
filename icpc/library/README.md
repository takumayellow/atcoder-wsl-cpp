# チームノート（library/）

本番はネット不可。ここのスニペットを **印刷（notebook/ で PDF 化）** ＋ **ローカル配置** の
両方で持ち込み、当日は**コードに貼り付けて**使う。

## 収録物

| 機能 | C++ (`cpp/`) | Python (`py/`) | 出典 |
|------|--------------|----------------|------|
| Union-Find | `dsu.hpp` | `dsu.py` | AC Library 抜粋 / 自前 |
| BIT（区間和） | `fenwick_tree.hpp` | `fenwick.py` | AC Library 抜粋 / 自前 |
| セグメント木 | `segtree.hpp` | `segtree.py` | 自前（非ACL・コンパクト版） |

## 使い方（C++ で ACL 抜粋を使うとき）

ICPC ジャッジに ACL は入っていないので `#include <atcoder/...>` は通らない。
2026ルール「外部ライブラリはソースに同梱して単体コンパイル可能なら可」に従い、
**使うヘッダの中身を提出ソースに貼り付ける**。

```cpp
#include <bits/stdc++.h>
using namespace std;

// ↓ library/cpp/dsu.hpp の中身をそのまま貼り付け
namespace atcoder { struct dsu { /* ... */ }; }

int main() {
    atcoder::dsu uf(n);   // 本番ジャッジでも単体コンパイル可
}
```

## 追加していく方針（両言語同等）

国内予選で出がちなもの。落穂ひろい的に増やす:
- 数論: `pow_mod` / `inv_mod` / 拡張ユークリッド / エラトステネス / 素因数分解
- グラフ: BFS/DFS, ダイクストラ, 0-1 BFS, トポロジカルソート, SCC
- 幾何: 点・ベクトル, ccw, 凸包, 線分交差（国内予選は幾何が出やすい）
- 文字列: Z-algorithm, ローリングハッシュ
- DP定石: ナップサック, LIS, bitDP

> ACL は Apache-2.0（再配布・改変可）。提出にライセンス表記は不要。
