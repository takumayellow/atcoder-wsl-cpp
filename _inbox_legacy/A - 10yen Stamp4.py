x, y = map(int, input().split())
if x >= y:
    print(0)
else:
    # 余りがない場合を先に判定し、そうでなければ +1
    print((y - x) // 10 + ([(y - x) % 10 == 0:0]))