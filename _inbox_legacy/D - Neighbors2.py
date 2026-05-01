class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1] * n

    def leader(self, a):
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x
        return

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

# 入力を受け取る
n, m = map(int, input().split())
uf = UnionFind(n + 1)
count = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    count[a] += 1
    count[b] += 1
    
    # 隣接数が3本以上の確認
    if count[a] >= 3 or count[b] >= 3:
        print("No")
        exit()

    # AとBがすでに連結かどうか確認
    if uf.same(a, b):
        print("No")
        exit()  # 括弧を追加

    # AとBを連結
    uf.merge(a, b)

# 条件を全て満たす場合
print("Yes")