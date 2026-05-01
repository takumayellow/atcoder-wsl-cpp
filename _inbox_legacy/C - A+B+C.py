n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
l=int(input())
c=list(map(int,input().split()))
q=int(input())
x=list(map(int,input().split()))
s=set()
for u in a:
    for v in b:
        for w in c:
            s.add(u+v+w)
for _ in x:
    print('NYoe s'[_ in s::2])