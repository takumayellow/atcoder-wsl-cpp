def char_to_num(char):
    if char == 'B':
        return 0
    elif char == 'W':
        return 1
    elif char == 'R':
        return 2

def compute_pyramid(n, input_str):
    # 初期変換
    x0 = [char_to_num(c) for c in input_str]
    
    # 階層ごとの計算（3で割った余りを使用）
    while len(x0) > 1:
        next_level = []
        for i in range(len(x0) - 1):
            sum_value = (x0[i] + x0[i + 1]) % 3
            next_value = (-sum_value) % 3
            next_level.append(next_value)
        x0 = next_level
    
    # 最終結果を数値から文字に変換
    final_value = x0[0]
    if final_value == 0:
        return 'B'
    elif final_value == 1:
        return 'W'
    elif final_value == 2:
        return 'R'

# 使用例
n = int(input())
input_str = input().strip()
print(compute_pyramid(n, input_str))
