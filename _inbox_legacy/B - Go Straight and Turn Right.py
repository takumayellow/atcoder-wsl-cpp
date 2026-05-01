n=int(input())
T=input()
x,y=0,0
dx,dy=1,0
for t in T:
    if t=="S":x,y=x+dx,y+dy
    else:dx,dy=dy,-dx
print(x,y)