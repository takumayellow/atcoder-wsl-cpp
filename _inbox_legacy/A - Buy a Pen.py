r,g,b=map(int,input().split())
c=input()
print(min(g,b) if c=="Red" else min(r,g) if c=="Blue" else min(r,b))