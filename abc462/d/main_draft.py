# ===========================================================================
# 【下書き / 提出前の素朴版（バグあり・記録用）】 ABC462 D - Accomplice
#
# このファイルは「最初に自分で書いた版」をそのまま残したもの。WA になる。
# 既知の問題点（詳細は explanation.md「7. 自分のコードの問題点」）:
#   1. デバッグ print が残っている → 出力が汚れて無条件 WA
#   2. l = T[i]-S[j] を while の外で1回しか計算しておらず、j を進めても固定（致命的）
#   3. 入力を S でソートしていない（式は S 昇順を前提にしている）
#   4. 全ペア列挙 O(N^2) で N≤2e5 では TLE
# → 同じ方針を正しく直したものは naive_fixed.py、本番解は main.cpp / editorial_evima.py。
#   実測: sample1 に 7 を出力（正解 4）。
# ===========================================================================

N, D = map(int, input().split())
S = []; T = []
for i in range(N):
    s, t = map(int, input().split())
    S.append(s); T.append(t)

count = 0

for i in range(N-1):
    j = i + 1
    l = T[i] - S[j]
    while ( l >= D and j <= N-1):
        count += max(0, min(l - (D -1),T[j]-S[j]-(D-1)))
        print(f"i,jの値は{i,j}")
        print(f"S[j],T[i]の値は{S[j],T[i]}")
        print(f"T[j]-S[j]-2は{T[j]-S[j]-(D-1)}")
        print(f"lの値は{l}")
        print(f"countの値は{count}")
        j += 1

print(count)

