S=input()[::-1]
p=""
for s in S:
    if s=="6":p+="9"
    elif s=="9":p+="6"
    else:p+=s
print(p)