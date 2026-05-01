n=int(input())
a=list(map(int,input().split()))
p=[0]*(n)
l0=[x for x in range(1,n+1)]

c=0

for i in range(n):
    if a[i]!=-1:
        if a[i] in p:print("No");break
        else:
            p[i]=a[i]
            pa=list(set(l0)-set(p))
            print(set(pa))

            c=0
            for i in range(n):
                if p[i]==0:p[i]=pa[c];c+=1
                print(p)