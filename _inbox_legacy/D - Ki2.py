n, q = map(int, input().split())
co = [[] for _ in range(n + 1)]  # 隣接リストを作成

for _ in range(n - 1):
    a, b = map(int, input().split())
    co[a].append(b)  # a と b を結ぶ辺を追加
    co[b].append(a)

c = [0] * (n + 1)  # カウンターを用意

for _ in range(q):
    p, x = map(int, input().split())
    c[p] += x  # p のカウンターに x を加算

from collections import deque
que = deque()
que.append(1)  # ルート頂点をキューに追加
visited = [False] * (n + 1)  # 訪問チェック用リスト
visited[1] = True  # ルートは訪問済みにする

while que:
    now = que.popleft()  # キューから頂点を取り出す
    now_number = c[now]  # 現在の頂点のカウンターの値を取得
    for to in co[now]:  # 現在の頂点に隣接する全頂点を調べる
        if not visited[to]:  # まだ訪問していない場合
            c[to] += now_number  # 現在のカウンターの値を加算
            visited[to] = True  # 訪問済みとしてマーク
            que.append(to)  # キューに追加

print(*c[1:])  # 各頂点のカウンターの値を出力