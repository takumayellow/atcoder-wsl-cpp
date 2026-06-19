# セグメント木（点更新・区間クエリ / 0-indexed・iterative） / 素の Python 3
# モノイド (op, e) を渡す。半開区間 [l, r)。
#
# 使い方の例（区間最小）:
#   seg = SegTree(n, op=min, e=float('inf'))
#   seg.build([...])         # 任意。初期配列があれば
#   seg.set(i, x)
#   seg.prod(l, r)
#
# 本番は import せず、このクラス本体を提出ソースへ貼り付ける。


class SegTree:
    def __init__(self, n, op, e):
        self.n = n
        self.op = op            # 結合的な二項演算（例: min, max, add, gcd）
        self.e = e              # 単位元（min なら inf, 和なら 0）
        self.t = [e] * (2 * n)

    def build(self, a):
        n = self.n
        for i in range(n):
            self.t[n + i] = a[i]
        for i in range(n - 1, 0, -1):
            self.t[i] = self.op(self.t[2 * i], self.t[2 * i + 1])

    def set(self, p, x):
        p += self.n
        self.t[p] = x
        p >>= 1
        while p:
            self.t[p] = self.op(self.t[2 * p], self.t[2 * p + 1])
            p >>= 1

    def get(self, p):
        return self.t[p + self.n]

    def prod(self, l, r):
        # 半開区間 [l, r)
        resl, resr = self.e, self.e
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                resl = self.op(resl, self.t[l])
                l += 1
            if r & 1:
                r -= 1
                resr = self.op(self.t[r], resr)
            l >>= 1
            r >>= 1
        return self.op(resl, resr)
