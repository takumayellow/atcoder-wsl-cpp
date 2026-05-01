h, w = map(int, input().split())
# 行列をリストのリストとして読み取る
matrix = [list(input().strip()) for _ in range(h)]
# すべての要素を1つのリストにフラット化
elements = [elem for row in matrix for elem in row]
# # の数をカウント
count = elements.count('#')
print(count)