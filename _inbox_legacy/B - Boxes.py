n = int(input())
l = list(map(int,input().split()))
if sum(l)% (((n)*(n+1))//2):
    print("NO")
else:
    k = sum(l) // (((n)*(n+1))//2)
    ll = [l[i]-l[i-1]-k for i in range(1,n)]
    if all(i % n == 0 for i in ll) and all(i <= 0 for i in ll):
        print("YES")
    else:
        print("NO")
