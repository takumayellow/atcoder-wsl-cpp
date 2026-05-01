s = input()

# '|' の位置をリストに格納
l = [i for i, char in enumerate(s) if char == '|']

# スライスで部分文字列を削除する
s = s[:l[0]] + s[l[1]+1:]

print(s)