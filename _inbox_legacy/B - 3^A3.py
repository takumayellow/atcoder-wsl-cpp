m=int(input())
A=[]
while m>0:
    a=0
    while 3**(a+1)<=m:
        a+=1
    A.append(a)
    m-=3**a
print(len(A))
print(*A)