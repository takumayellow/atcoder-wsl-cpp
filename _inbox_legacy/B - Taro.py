n,m=map(int,input().split())
l=[0]*n
for i in range(1,m+1):
        # 入力を受け取る
    input_line = input()  # "1 M" みたいなやつ

    # 空白で分けてリストにする
    num_str = input_line.split()  # ['1', 'M'] になるよ！

    # 最初の部分を整数に変換して、次の部分を文字列としてそのまま使う
    a = int(num_str[0])  # '1' を整数 1 に変換
    b = num_str[1]  # 'M' はそのまま
    if b=="M" and l[a-1]==0:l[a-1]+=i
for i in range(1,m+1):
    if l.count(i)==1:print("Yes")
    else:print("No")