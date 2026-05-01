s=input()
a,b=map(int, input().split())
print(s.replace(s[a-1],"A").replace(s[b-1],s[a-1]).replace("A",s[b-1]))