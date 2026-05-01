n = int(input())
m = [list(map(int, input().split())) for _ in range(n-1)]
flat_list = [element for row in m for element in row]  # これでリストをフラットにするよ
total_sum = sum(flat_list)
expected_sum = n * (n + 1) // 2
result = (total_sum - expected_sum) / (n - 2)
print('NYoe s'[int(result.is_integer())::2])