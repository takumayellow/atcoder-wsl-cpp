n,m=map(int,input().split())
a=list(map(int,input().split()))
indices = [*range(len(a))]
sorted_indices = sorted(indices, key=lambda i: a[i])
sorted_a = [a[i] for i in sorted_indices]
print(indices)
print(sorted_indices)
print(sorted_a)
b=list(map(int,input().split()))
for j in range(m):
    high=n
    low=0
    mid=(high+low)//2
    while low+1<high:
        mid_person=sorted_a[mid]
        if mid_person<b[j]:
            high=mid
        else:
            low=mid
        mid=(low+high)//2
    if mid>0:print(sorted_indices[mid]);sorted_a[mid]=0
    else:print(-1)