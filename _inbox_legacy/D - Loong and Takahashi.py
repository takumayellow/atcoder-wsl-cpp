n=int(input())
a=[[0]*n for _ in range(n)]
y,x,c=0,-1,0
for i in range(n//2):
    for j in range(n-i*2):
        x+=1
        c+=1
        a[y][x]=c
    for j in range(n-i*2-1):
        y+=1
        c+=1
        a[y][x]=c
    for j in range(n-i*2-1):
        x-=1
        c+=1
        a[y][x]=c
    for j in range(n-i*2-2):
        y-=1
        c+=1
        a[y][x]=c
a[y][x+1]="T"
for r in a:print(*r)