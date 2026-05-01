a, b = map(int, input().split())
# a * b % 2 == 1 が True の場合には 'Odd' を、False の場合には 'Even' を取得する
result = "OddEven"[a * b % 2 * 4::4]
print(result)