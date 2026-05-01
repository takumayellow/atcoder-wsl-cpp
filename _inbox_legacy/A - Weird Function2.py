def a(t):
    return t**2+2*t+3
x=int(input())
k=a(a(a(x)+x)+a(a(x)))
print(k)