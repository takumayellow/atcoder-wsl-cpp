A=int(input())
N=[0]*A
for i in range(A-1):
    X,Y=map(int,input().split())
    N[X-1]+=1
    N[Y-1]+=1
F=False
for i in range(A):
    if N[i]==A-1:
        F=True
if F==True:
    print("Yes")
else:
    print("No")