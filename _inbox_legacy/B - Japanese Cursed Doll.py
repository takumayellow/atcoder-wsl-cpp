n, t, p = map(int, input().split())
l = list(map(int, input().split()))

# すでに髪の長さが T 以上の人の人数を数える
count = sum(1 for x in l if x >= t)

# もしすでに P 人以上いれば 0 を出力して終了
if count >= p:
    print(0)
else:
    # 日数 d を増やしながら条件を満たす日を探す
    for d in range(1, 101):  # 最大でも 100 日後には全員 T 以上になる
        count = sum(1 for x in l if x + d >= t)
        if count >= p:
            print(d)
            break