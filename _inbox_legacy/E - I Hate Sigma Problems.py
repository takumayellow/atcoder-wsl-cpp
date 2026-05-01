
# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 種類数を管理するための辞書
count = {}

# 答えを格納する変数
total = 0

# 右端を示すポインタ
right = 0

# 種類数を示す変数
unique_count = 0

# 左端を1つずつ動かす
for left in range(N):
    # rightをできるだけ右に進めて、種類数を数える
    while right < N:
        # 要素A[right]が初めてなら種類数を増やす
        if count.get(A[right], 0) == 0:
            unique_count += 1
        
        # 要素A[right]をカウントする
        count[A[right]] = count.get(A[right], 0) + 1
        right += 1
        
        # 条件が満たされなくなったらループを抜ける
        if right == N or count.get(A[right], 0) > 0:
            break
    
    # (left, right-1)の区間の種類数を加算する
    total += unique_count
    
    # A[left]を区間から外すので、カウントを減らす
    count[A[left]] -= 1
    if count[A[left]] == 0:
        unique_count -= 1

# 結果を出力
print(total)
