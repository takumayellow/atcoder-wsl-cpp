# 入力を受け取る
a, b = map(int, input().split())
e = [0] * (a + b)

# AがB以上の場合
if a >= b:
    # 正の整数を配置
    for i in range(a):
        e[i] = i + 1
    # 負の整数を配置
    for i in range(b - 1):
        e[i + a] = -(i + 1)
    # 最後の要素を調整して合計を0に
    e[a + b - 1] = -(sum(e[:a + b - 1]))

# AがB未満の場合
else:
    # 正の整数を配置
    for i in range(a - 1):
        e[i] = i + 1
    # 負の整数を配置
    for i in range(b):
        e[i + a] = -(i + 1)
    # 最後の要素を調整して合計を0に
    e[a - 1] = -(sum(e[:a + b]))

# 出力
print(" ".join(map(str, e)))