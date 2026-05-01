# 入力を受け取る
s = input()
t = input()

# @で置き換え可能な文字
replaceable_chars = set("atcoder")

# 各文字を比較
for i in range(len(s)):
    # s[i] と t[i] が異なる場合の処理
    if s[i] != t[i]:
        # どちらも @ ではないし、置き換え可能な文字でもないなら負け
        if s[i] != "@" and t[i] != "@" or \
           (s[i] == "@" and t[i] not in replaceable_chars) or \
           (t[i] == "@" and s[i] not in replaceable_chars):
            print("You will lose")
            break
# すべての文字が条件を満たすなら勝ち
else:
    print("You can win")