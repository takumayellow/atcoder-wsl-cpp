S = input()
P = "Hello,World!"

# 長さが異なる場合は即座に不正を出力
if len(S) != len(P):
    print("WA")
else:
    # 1文字ずつ比較して一致しなければすぐに終了
    for i in range(len(S)):
        if S[i] != P[i]:
            print("WA")
            break
    else:
        # for文が正常に終了した場合
        print("AC")