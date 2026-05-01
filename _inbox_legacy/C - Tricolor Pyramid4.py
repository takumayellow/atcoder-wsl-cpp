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

    # 階層ごとの計算
    current_level = x0
    while len(current_level) > 1:
        next_level = []
        for i in range(len(current_level) - 1):
            sum_value = current_level[i] + current_level[i + 1]
            if (sum_value % 3) == 0:
                next_value = sum_value
            else:
                next_value = -1 * sum_value
            next_level.append(next_value)
        current_level = next_level
    
    # 最終結果を 3 で割った余りに変換
    final_value = current_level[0] % 3
    
    # 数値を文字に変換
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