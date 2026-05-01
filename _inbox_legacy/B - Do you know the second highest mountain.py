n = int(input())
data = [tuple(input().split()) for _ in range(n)]
data = [(int(t), s) for s, t in data]  # 高さをint型に変換

data.sort(reverse=True)  # 高さを基準に降順ソート

print(data[1][1])  # 2番目の山の名前を出力
