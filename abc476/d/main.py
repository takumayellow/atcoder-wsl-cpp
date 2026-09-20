# ABC476 D - Automat（ドリンクを買う部分まで書いた途中のメモ。提出したものではない）
#
# 完成版は main.cpp（商品を 1 つの袋にまとめる版）と explained.py / sub.py / src.py
# （ドリンクの本数で全探索する版）。このファイルは残り 3 点が未着手:
#   - デザートを買う処理がまだ無い（最後の print はデバッグ出力）
#   - 判定が y > s になっている（ちょうど使い切るケースを落とすので y >= s が正しい）
#   - お釣りの計算が s - b[i] になっている（1 ドル札で戻るのは s*k - b[i]）

import math
n, m, k = map(int,input().split())
x, y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a = sorted(a)
b = sorted(b)

count = 0

for i in range(m):
    s = math.ceil(b[i]/k)
    if (y > s):
        y -= s
        x += s - b[i]
        print(x)
        count += 1
    else: break

print(x,y,count)


