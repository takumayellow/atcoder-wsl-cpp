# Union-Find（素集合データ構造） / 素の Python 3（NumPy不可）
# 使い方: d = DSU(n); d.merge(a, b); d.same(a, b); d.size(a); d.leader(a)
# 本番は import せず、このクラス本体を提出ソースへ貼り付ける。


class DSU:
    def __init__(self, n):
        # root: -size（負）, それ以外: 親の index
        self.p = [-1] * n

    def leader(self, a):
        # 経路圧縮（反復版・再帰上限回避）
        while self.p[a] >= 0:
            if self.p[self.p[a]] >= 0:
                self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return x
        if -self.p[x] < -self.p[y]:  # 小さい方を大きい方へ（union by size）
            x, y = y, x
        self.p[x] += self.p[y]
        self.p[y] = x
        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return -self.p[self.leader(a)]
