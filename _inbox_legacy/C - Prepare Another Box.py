n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a と b をソートしておく
a.sort()
b.sort()

def can_succeed_with_x(x):
    # b に x を追加し、ソートする
    extended_b = b + [x]
    extended_b.sort()
    
    j = 0
    # 各 a[i] に対して、b[j] が適切か確認する
    for i in range(n):
        # a[i] に対して、b[j] がそれ以上の値になるまで j を進める
        while j < len(extended_b) and extended_b[j] < a[i]:
            j += 1
        # 適切な b[j] がなければ失敗
        if j == len(extended_b):
            return False
        # 使った b[j] は次回使えないので j を進める
        j += 1
    return True  # すべての a[i] に適切な b[j] があれば成功

# x の最小値を二分探索で探す
left, right = 1, max(a) + 1
while left < right:
    mid = (left + right) // 2
    if can_succeed_with_x(mid):
        right = mid  # 成功した場合、x の最小値をさらに小さく探す
    else:
        left = mid + 1  # 失敗した場合、x を大きくする

# 最後に成功する x が見つかっていればその値を出力、そうでなければ -1
if can_succeed_with_x(left):
    print(left)
else:
    print(-1)
