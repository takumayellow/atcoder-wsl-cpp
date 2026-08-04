import math

a = 4321214
b = 7645735



for x in range(10**18):
    for y in range(10**18):
        if gcd(a+x, b+y)!=1:print((x,y,gcd(a+x,b+y))) 
