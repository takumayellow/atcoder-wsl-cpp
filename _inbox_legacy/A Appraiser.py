N,M,Q=map(int,input().split())
n=N-Q
m=M

ans=[]
for i in range(n):
    if i==n-1 and sum(ans)==0:
        for j in range(2*m-1):
            print("?",1,2*m*i+j+1)
            ans.append(int(input()))
        ans.append(m-sum(ans))
    else:
        A=[0]
        for j in range(2*m-1):
            print("?",2*m*i+j+1,2*m*i+j+2)
            A.append((A[-1]+int(input()))%2)

        if sum(A)<m:
            for a in A:
                ans.append(a)
        elif sum(A)>m:
            for a in A:
                ans.append(1-a)
        else:
            print("?",2*i+1,N)
            if int(input())==0:
                for a in A:
                    ans.append(a)
            else:
                for a in A:
                    ans.append(1-a)
            break

ansstr="! "
for i in range(len(ans)):
    if ans[i]==1:
        ansstr+=str(i+1)+" "
print(ansstr)