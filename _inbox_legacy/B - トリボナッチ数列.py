n = int(input())

# nが1, 2, 3の場合の処理
if n == 1:
    print(0)
elif n == 2:
    print(0)
elif n == 3:
    print(1)
else:
    # 配列を用意（0を3つ以上確保）
    a = [0] * (n + 1)
    a[1], a[2], a[3] = 0, 0, 1

    # トリボナッチ数列を計算
    for i in range(4, n + 1):
        a[i] = (a[i - 1] + a[i - 2] + a[i - 3]) % 10007

    # 結果を出力
    print(a[n])
