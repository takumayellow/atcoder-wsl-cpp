n = int(input())
s = list(map(int, input().split()))
ans = 0

# 各面積について検証する
for Si in s:
    found = False  # 現在の面積が正しいかどうかを示すフラグ
    for a in range(1, 334):  # a を 1 から 333 まで
        for b in range(1, 334):  # b を 1 から 333 まで
            if Si == 4 * a * b + 3 * a + 3 * b:
                found = True  # 面積が正しい場合
                break  # 正しい組み合わせが見つかったので、これ以上は調べない
        if found:
            break  # a に対して正しい b が見つかったので、次の Si へ進む
    if not found:  # もし、正しい組み合わせが見つからなかった場合
        ans += 1  # 確実に誤りである人数をカウント

print(ans)