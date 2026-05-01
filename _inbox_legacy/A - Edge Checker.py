a,b=map(int,input().split())
if a==10 or b==10:
    print("YNeos"[abs(b-a)!=1 and abs(b-a)!=9::2])
else: print("YNeos"[abs(b-a)!=1::2])