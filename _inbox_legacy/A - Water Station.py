n=int(input())
m=0
for i in range(21):
    if abs(5*(i+1)-n)<abs(5*i+-n): m=i+1
print(5*m)