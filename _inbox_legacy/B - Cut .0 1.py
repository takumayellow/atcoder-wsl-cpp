x=list(input())
while x[-1]=="0":x.pop()
if x[-1]==".":x.pop()
print("".join(x))