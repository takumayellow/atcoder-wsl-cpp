// 自前セグメント木（非ACL・コンパクト版 / 0-indexed・iterative）
// 点更新・区間クエリ。モノイド (op, e) をテンプレート引数で渡す。
// ACL の segtree より短くて貼りやすい。半開区間 [l, r)。
//
// 使い方の例（区間最小）:
//   long long op(long long a, long long b){ return std::min(a, b); }
//   long long e(){ return LLONG_MAX; }
//   SegTree<long long, op, e> seg(n);   // または SegTree<...> seg(vec);
//   seg.set(i, x);  seg.prod(l, r);

#include <vector>

template <class S, S (*op)(S, S), S (*e)()>
struct SegTree {
    int n;
    std::vector<S> t;

    explicit SegTree(int n_) : n(n_), t(2 * n_, e()) {}
    explicit SegTree(const std::vector<S>& a) : n((int)a.size()), t(2 * a.size()) {
        for (int i = 0; i < n; i++) t[n + i] = a[i];
        for (int i = n - 1; i >= 1; i--) t[i] = op(t[2 * i], t[2 * i + 1]);
    }

    // 位置 p を値 x に更新
    void set(int p, S x) {
        for (t[p += n] = x; p >>= 1;) t[p] = op(t[2 * p], t[2 * p + 1]);
    }

    S get(int p) const { return t[p + n]; }

    // 半開区間 [l, r) の畳み込み
    S prod(int l, int r) const {
        S resl = e(), resr = e();
        for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
            if (l & 1) resl = op(resl, t[l++]);
            if (r & 1) resr = op(t[--r], resr);
        }
        return op(resl, resr);
    }
};
