# 入力の読み取り
n = int(input())
s = 0  # A君の得点
t = 0  # B君の得点

# 各ラウンドの結果を処理
for _ in range(n):
    a, b = map(int, input().split())
    
    # 得点の計算
    if a > b:
        s += a  # A君の方が強い場合
    elif a < b:
        t += b  # B君の方が強い場合
    # 同点の場合は得点の加算はなし

# 結果を出力
print(max(s, t))  # 勝者の点数を出力