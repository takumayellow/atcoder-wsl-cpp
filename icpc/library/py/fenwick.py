# Fenwick Tree / BIT（区間和） / 素の Python 3
# 使い方: ft = Fenwick(n); ft.add(i, x); ft.sum(l, r)  # 半開区間 [l, r)
# 本番は import せず、このクラス本体を提出ソースへ貼り付ける。


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.d = [0] * (n + 1)  # 1-indexed 内部配列

    def add(self, p, x):
        # 位置 p（0-indexed）に x を加算
        p += 1
        while p <= self.n:
            self.d[p] += x
            p += p & -p

    def _sum(self, r):
        # [0, r) の和
        s = 0
        while r > 0:
            s += self.d[r]
            r -= r & -r
        return s

    def sum(self, l, r):
        # 半開区間 [l, r) の和
        return self._sum(r) - self._sum(l)
