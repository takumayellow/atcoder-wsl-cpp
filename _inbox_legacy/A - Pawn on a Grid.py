h, w = map(int, input().split())
s = [input().strip() for _ in range(h)]
count = sum(row.count("#") for row in s)
print(count)