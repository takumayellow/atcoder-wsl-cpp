n=int(input())
h=list(map(int,input().split()))
a=h[0]
for i in range(0,n-1):
    if h[i]<h[i+1]:a=h[i+1]
    else:break
print(a)