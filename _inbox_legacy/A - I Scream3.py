# 元の if-elif コード
def original_code(a, b):
    x = a + b
    if x >= 15 and b >= 8:
        return 1
    elif x >= 10 and b >= 3:
        return 2
    elif x >= 3:
        return 3
    else:
        return 4

# ゴルフしたコード
def golf_code(a, b):
    return 4 - (a + b >= 15 and b >= 8) * 1 - (a + b >= 10 and b >= 3) * 2 - (a + b >= 3)

# テスト用データ
test_cases = [
    (16, 1),
    (10, 5),
    (4, 4),
    (1, 1),
    (8, 8),
    (0, 3),
    (5, 10),
    (3, 2),
    (15, 8),
]

# テスト実行
results = []
for a, b in test_cases:
    expected = original_code(a, b)
    actual = golf_code(a, b)
    results.append((a, b, expected, actual, expected == actual))

# 結果表示
for a, b, expected, actual, match in results:
    print(f"a={a}, b={b} → Expected: {expected}, Actual: {actual}, Match: {match}")
