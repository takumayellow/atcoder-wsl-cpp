N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

# 医師の総数チェック
total_doctors = sum(A)
if total_doctors < N:
    print(-1)
    exit()

# 初期マスと医師の数をマス順にまとめてソート
positions = sorted((X[i] - 1, A[i]) for i in range(M))  # 0-indexed
operations = 0
required_doctors = 0  # 不足している医師数を管理

# 各マスを順に確認しながら、必要な医師数を適切に配置
for i in range(N):
    if positions and positions[0][0] == i:
        # 現在のマスに医師がいる場合
        current_doctors = positions[0][1]
        positions.pop(0)  # 処理済みとして除去
    else:
        current_doctors = 0

    # 必要な医師の数と余剰の医師数を更新
    if current_doctors + required_doctors >= 1:
        # 十分な医師がある場合
        operations += abs(required_doctors)  # 移動回数をカウント
        required_doctors = current_doctors + required_doctors - 1
    else:
        # 不足する場合、必要数を増やす
        required_doctors -= 1

# すべてのマスに1個ずつ配置できるかを確認
print(operations if required_doctors == 0 else -1)
