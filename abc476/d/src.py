# ABC476 D - Automat（ゴルフ版。読みやすく展開したものが explained.py）
#
# ドリンクを安い順に 0, 1, 2, ... 本買う場合を全部試す。
#   a  : デザートを安い順に並べた累積和（bisect で「予算以下の個数」を引く）
#   t  : ここまでに買ったドリンクの本数
#   q  : ドリンク 1 本に必要な K ドル札の枚数 = ceil(v/k) を -(-v//k) で計算
#   x + k*y : 所持金の総額。ドリンクを買うとちょうど v だけ減る（お釣りは 1 ドル札）
# 先頭の [0] はダミーで、ループ 1 週目が「ドリンク 0 本」の場合に対応する。
# v > k*y は ceil(v/k) > y と同値で、K ドル札が足りないことを意味する。

from bisect import*
(n, m, k), (x, y), a, b = [map(int, o.split()) for o in open(0)]
S = sorted;z=t=s=0;a=[s:=s+v for v in S(a)]
for v in[0]+S(b):
    if v>k*y:break
    q=-(-v//k);y-=q;x+=q*k-v;z=max(z,t+bisect(a,x+k*y));t+=1
print(z)
