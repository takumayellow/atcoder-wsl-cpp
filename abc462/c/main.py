import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n)]
    # X 昇順にソートし、Y の prefix minimum を更新した回数を数える。
    # 点 i が条件を満たす <=> 自分より真に左下 (Xj<Xi かつ Yj<Yi) の点が無い。
    pts.sort(key=lambda p: p[0])
    ans = 0
    min_y = float("inf")
    for _, y in pts:
        if y < min_y:
            ans += 1
            min_y = y
    print(ans)


if __name__ == "__main__":
    main()
