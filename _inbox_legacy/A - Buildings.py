n = int(input())
h = list(map(int, input().split()))

# 1からn-1までの範囲でループ
for i in range(1, n):
    if h[i] > h[0]:  # 0番目の要素と比較
        print(i + 1)  # 1-based indexで出力するためにi+1
        break
else:
    print(-1)  # どの要素も条件に合わなければ-1を出力