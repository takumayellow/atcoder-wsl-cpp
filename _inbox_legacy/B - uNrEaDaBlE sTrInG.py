s = input()

def is_unreadable_string(s):
    for i in range(len(s)):
        if i % 2 == 0:  # 奇数番目（0-indexed）
            if not s[i].islower():  # 小文字でなければならない
                return False
        else:  # 偶数番目（0-indexed）
            if not s[i].isupper():  # 大文字でなければならない
                return False
    return True

if is_unreadable_string(s):
    print("Yes")
else:
    print("No")