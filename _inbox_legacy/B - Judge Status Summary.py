n=int(input())
c_0=0
c_1=0
c_2=0
c_3=0
for i in range(n):
    s=input()
    if s=="AC":
        c_0+=1
    elif s=="WA":
        c_1+=1
    elif s=="TLE":
        c_2+=1
    else:c_3+=1
print(f"AC x {c_0}")
print(f"WA x {c_1}")
print(f"TLE x {c_2}")
print(f"RE x {c_3}")