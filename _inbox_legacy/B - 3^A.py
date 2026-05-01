m=int(input())
a=[]
for i in range(11):
    while m>=3**(10-i):a.append(10-i);m-=3**(10-i)
print(len(a))
print(*a)