t = input()

# 1. 長さが偶数でなければ "No"
if len(t) % 2 != 0:
    print("No")
else:
    is_1122_string = True

    # 2. 各ペアが一致しているかチェック
    for i in range(len(t) // 2):
        if t[2 * i] != t[2 * i + 1]:
            is_1122_string = False
            break

    # 3. 各文字がちょうど2回現れるかチェック
    if is_1122_string:
        for char in set(t):  # 一意な文字だけチェック
            if t.count(char) != 2:
                is_1122_string = False
                break

    # 結果を出力
    print("Yes" if is_1122_string else "No")
