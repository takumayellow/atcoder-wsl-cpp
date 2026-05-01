# 入力の受け取り
n = int(input())  # 投票人数
votes = [input().strip() for _ in range(n)]  # 各人の投票先をリストとして取得

# 得票数をカウントする辞書
vote_count = {}

# 投票をカウント
for vote in votes:
    if vote in vote_count:
        vote_count[vote] += 1
    else:
        vote_count[vote] = 1

# 最大得票数の候補者を見つける
max_votes = -1
winner = ""

for candidate, count in vote_count.items():
    if count > max_votes:
        max_votes = count
        winner = candidate

# 得票数が最大の候補者を出力
print(winner)