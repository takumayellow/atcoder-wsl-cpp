def main():
    S = input().strip()
    for T in ["oxx", "xox", "xxo"]:
        ok = True
        for i in range(len(S)):
            if T[i % 3] != S[i]:
                ok = False
                break
        if ok:
            print("Yes")
            return
    print("No")

main()
