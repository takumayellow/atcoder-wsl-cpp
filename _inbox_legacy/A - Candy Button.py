n, c = map(int, input().split())
t = list(map(int, input().split()))  # ボタンが押された時刻のリスト
count = 1  # 最初のボタンは必ず押されるのでカウントは1から
last_t = t[0]  # 最初のボタンを押した時刻
for i in range(n - 1):
    if t[i + 1] - last_t >= c:
        count += 1
        last_t = t[i + 1]  # 次の押された時刻を更新
print(count)
