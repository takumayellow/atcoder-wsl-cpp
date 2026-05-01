n = int(input())  # 拠点の数
employees = []  # 各拠点の社員数と現地時刻を格納するリスト

# 各拠点の社員数と現地時刻を入力
for _ in range(n):
    w, x = map(int, input().split())
    employees.append((w, x))

max_attendees = 0  # 参加可能な社員数の最大値

# UTC時間帯0〜23について、それぞれで会議を開催したときの社員数を計算
for utc_time in range(24):
    attendees = 0  # その時間帯で参加できる社員数
    for w, x in employees:
        # 拠点xの現地時間で9:00～18:00に当たるUTC時間帯を計算
        local_start = (9 - x) % 24
        local_end = (18 - x) % 24
        
        # 現在のUTC時間がこの拠点の参加可能な時間帯に含まれているかを確認
        if local_start <= local_end:
            if local_start <= utc_time < local_end:
                attendees += w
        else:
            if utc_time >= local_start or utc_time < local_end:
                attendees += w

    # 参加可能な社員数の最大値を更新
    max_attendees = max(max_attendees, attendees)

print(max_attendees)