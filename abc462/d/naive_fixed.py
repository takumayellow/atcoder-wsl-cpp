# ===========================================================================
# ABC462 D - Accomplice  /  自分のアルゴリズム（ペア全列挙）を正しく直した版
#
# 方針は下書き(main_draft.py)と同じ「ペア (i, j) を直接列挙して、その2人で
# 成立する犯行開始時刻 x の個数を足し込む」。下書きの3つのバグを修正した：
#   ① 入力を S（入室時刻）の昇順にソート         … 寄与式が S_i ≤ S_j を前提にするため
#   ② l = T[i] - S[j] をペアごとに毎回計算し直す   … 下書きは while の外で固定していた
#   ③ デバッグ print を全削除                     … 出力を汚さない
#
# 【ペア (i, j) の寄与（= その2人で成立する開始時刻 x の個数）】
#   2人が同時に居る区間は [max(S_i,S_j), min(T_i,T_j)]。
#   開始 x は x..x+D が両者の在室に収まる必要があるので
#       x ∈ [max(S_i,S_j),  min(T_i,T_j) − D]
#   個数 = max(0, min(T_i,T_j) − max(S_i,S_j) − D + 1)
#   S 昇順ソート済みなら max(S_i,S_j) = S_j（j が後ろ＝開始が遅い）なので、
#   下書きと同じ形 min(T_i−S_j, T_j−S_j) − (D−1) で書ける。
#
# 【計算量】O(N^2)。N ≤ 2×10^5 では TLE するので本番提出には使えない。
#   → 小さい N での「答え合わせ用」。本番解は main.cpp / editorial_evima.py（O(N+maxT)）。
# ===========================================================================

import sys
input = sys.stdin.readline

N, D = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]
P.sort()                      # ① S（次に T）の昇順に並べる

count = 0
for i in range(N):
    Si, Ti = P[i]
    for j in range(i + 1, N):
        Sj, Tj = P[j]
        l = Ti - Sj           # ② ペアごとに毎回計算（重なりの右側の余裕）
        if l < D:
            # S 昇順なので、これ以降の j はさらに Sj が大きく重なりも減るだけ。
            # よってこの i についてはもう寄与が出ない → break で打ち切り（枝刈り）。
            break
        # min(T_i,T_j) − S_j − D + 1 を、下書きと同じ形で計算（負なら0）
        count += max(0, min(l - (D - 1), Tj - Sj - (D - 1)))

print(count)
