x, y = map(int, input().split())
if x >= y:
    print(0)
else:
    # 条件に応じて 1 または 0 を足す処理
    print((y - x) // 10 + [0, 1][(y - x) % 10 != 0])