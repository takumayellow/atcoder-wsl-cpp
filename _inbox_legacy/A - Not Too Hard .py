N, X= map(int, input().split())
S_lst= list(map(int, input().split(" ")))
sum_val = 0
for s in S_lst:
    if s <= X:
        sum_val += s
print(sum_val)