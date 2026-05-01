def char_to_num(char):
    if char == 'B':
        return 0
    elif char == 'W':
        return 1
    elif char == 'R':
        return -1

def mod3(x):
    result = x % 3
    if result == 2:
        return -1
    return result

def num_to_char(num):
    if num == 0:
        return 'B'
    elif num == 1:
        return 'W'
    elif num == -1:
        return 'R'

n = int(input())  # 文字列の長さ
input_str = input()  # 文字列

# 文字列を数値に変換
x0 = [char_to_num(char) for char in input_str]

# ピラミッド構造の計算を開始
pyramid = [x0]  # 最下段から開始

for j in range(n - 1):
    current_level = pyramid[-1]
    next_level = []
    for i in range(len(current_level) - 1):
        # 修正された漸化式の計算
        next_value = (current_level[i] + current_level[i + 1])
        # mod3を適用して結果を調整
        next_level.append(mod3(next_value))
    pyramid.append(next_level)

# ピラミッドの頂点の値を文字に変換して出力
print(num_to_char(pyramid[-1][0]))  # 最上段の唯一の要素を出力
