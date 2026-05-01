# 入力を取得
K = int(input())

# A から K 番目までのアルファベットを生成
x = [chr(i) for i in range(65, 65 + K)]

# 文字列 P を空の文字列で初期化
P = ''

# 各文字を P に追加
for i in range(K):
    P += x[i]

print(P)