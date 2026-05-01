N = int(input())
H = list(map(int, input().split()))

# 結果を格納する配列
result = [0] * N

# スタックを使って右側のビルの情報を管理
stack = []

# 右から左へ処理を進める
for i in range(N - 1, -1, -1):
    # 現在のビルよりも低いビルをすべてスタックから取り除く
    while stack and H[i] > H[stack[-1]]:
        stack.pop()

    # 条件を満たすビルの個数はスタックに残っている要素の数
    result[i] = len(stack)

    # 現在のビルのインデックスをスタックに追加
    stack.append(i)

# 結果を出力
print(*result)
