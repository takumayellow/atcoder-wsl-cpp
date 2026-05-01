n=int(input())
s=[input().strip() for _ in range(n)]
count=0
for i in range(n):
    if s[i]=="For": count+=1
print("YNeos"[count<(-~n//2)::2])