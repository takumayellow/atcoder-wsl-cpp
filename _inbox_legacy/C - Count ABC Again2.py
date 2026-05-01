n, q = map(int, input().split())
s = list(input())  # 文字列をリストに変換して、効率よく1文字を置き換える
count = 0

# 初期の "ABC" の数をカウント
for i in range(n-2):
    if s[i:i+3] == ['A', 'B', 'C']:
        count += 1

# 結果を出力するリスト
result = []

# ヘルパー関数で3文字の部分をチェックする
def check_abc(i):
    if i < 0 or i > n - 3:
        return 0
    return 1 if s[i:i+3] == ['A', 'B', 'C'] else 0

# クエリ処理
for _ in range(q):
    x, c = input().split()
    x = int(x) - 1
    
    # 変更前後の周辺を確認
    for i in range(x-2, x+1):
        count -= check_abc(i)  # 変更前の "ABC" を減らす

    s[x] = c  # 指定位置の文字を変更

    for i in range(x-2, x+1):
        count += check_abc(i)  # 変更後の "ABC" を追加

    result.append(count)

print(*result, sep="\n")