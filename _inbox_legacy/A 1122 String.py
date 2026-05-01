n=int(input())
t = input()
if len(t) % 2 == 0:
    print("No")
else:
    mid = (len(t) + 1) // 2 - 1  # 整数にするため「//」を使う
    for i in range(mid):
        if t[i] != "1":
            print("No")
            break
    else:
        if t[mid] != "/":
            print("No")
        else:
            for i in range(mid + 1, len(t)):
                if t[i] != "2":
                    print("No")
                    break
            else:
                print("Yes")
