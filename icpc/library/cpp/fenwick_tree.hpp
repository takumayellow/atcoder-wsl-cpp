// AC Library 抜粋: Fenwick Tree / BIT (atcoder/fenwicktree.hpp 簡約)
// 出典: https://github.com/atcoder/ac-library (Apache-2.0)
// 使い方: fenwick_tree<long long> ft(n); ft.add(i, x); ft.sum(l, r);  // 半開区間 [l, r)
// 本番では namespace atcoder { ... } ごと提出ソースへ貼り付ける。

#include <cassert>
#include <vector>

namespace atcoder {

template <class T> struct fenwick_tree {
  public:
    fenwick_tree() : _n(0) {}
    explicit fenwick_tree(int n) : _n(n), data(n) {}

    void add(int p, T x) {
        assert(0 <= p && p < _n);
        p++;
        while (p <= _n) {
            data[p - 1] += x;
            p += p & -p;
        }
    }

    // 半開区間 [l, r) の和
    T sum(int l, int r) {
        assert(0 <= l && l <= r && r <= _n);
        return sum(r) - sum(l);
    }

  private:
    int _n;
    std::vector<T> data;

    T sum(int r) {
        T s = 0;
        while (r > 0) {
            s += data[r - 1];
            r -= r & -r;
        }
        return s;
    }
};

}  // namespace atcoder
