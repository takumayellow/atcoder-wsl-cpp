def mod3(x):
    result = x % 3
    # 余りが2なら-1に変換
    if result == 2:
        return -1
    return result

# # テスト例
# numbers = [4, 7, 9, -5]
# converted = [mod3(x) for x in numbers]
# print(converted)  # 出力: [1, 1, 0, -1]

n=int(input())
x0=list(map(int,input().split()))
x0mod3=[mod3(x) for x in x0]
for j in range(n-1):
    for i in range(n-1-j):
        x_(j+1)[i]=x_j[i]+x_j[i+1]*((-1)**(x_j[i]+x_j[i+1]))
pprint(x_n[0])