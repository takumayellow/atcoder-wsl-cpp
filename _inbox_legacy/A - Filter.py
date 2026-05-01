n = int(input())  # リストのサイズを取得
a = list(map(int, input().split()))  # 数値リストを取得

p = []  # 空のリストを作成

for x in a:  # リスト a の各要素に対してループ
    if x % 2 == 0:  # 偶数かどうかをチェック
        p.append(x)  # 偶数の場合はリスト p に追加

# 空白区切りの文字列に変換して出力
print(' '.join(map(str, p)))