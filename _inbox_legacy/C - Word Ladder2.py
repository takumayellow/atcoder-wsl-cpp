S,T=input(),input()
N=len(S)
X=[]
while S!=T:
    nS="z"*N
    for i in range(N):
        if S[i]!=T[i]:
            nS=min(nS,S[:i]+T[i]+S[i+1:])
    X.append(nS)
    S=nS
print(len(X))
for x in X:
    print(x)