N = int(input())  # 部署の数
K = list(map(int, input().split()))  # 各部署の人数

total_sum = sum(K)  # 全体の人数の合計
min_max_lunch = total_sum  # 同時に昼休みを取る最大人数を最小化したい

# bit全探索: 部署をグループAとBに分ける方法を全探索
for i in range(1 << N):
    group_a_sum = 0
    for j in range(N):
        if i & (1 << j):  # j番目の部署がグループAに属する場合
            group_a_sum += K[j]
    group_b_sum = total_sum - group_a_sum  # グループBの人数は全体からAを引いたもの
    min_max_lunch = min(min_max_lunch, max(group_a_sum, group_b_sum))

print(min_max_lunch)
