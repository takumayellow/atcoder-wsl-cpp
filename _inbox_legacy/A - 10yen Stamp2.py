x, y = map(int, input().split())
if x >= y:
    print(0)
else:
    # 割り算の余りがあるかどうかで判定
    print((y - x) // 10 + (1 if (y - x) % 10 != 0 else 0))