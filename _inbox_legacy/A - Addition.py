n = int(input())
arr = list(map(int, input().split()))

no_odds = 0
for val in arr:
    if val & 1:
        no_odds += 1
if no_odds &1:
    print("NO")

else:
    print("YES")