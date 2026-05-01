def divisor_cs(num):
    cnt = 0
    sigma = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            cnt += 1
            sigma += i
            if i**2 == num:
                continue
            cnt +=1
            sigma+=(int(num/i))  
    return cnt,sigma
                            
n=int(input())
s=0
for i in range(n):
    cnt,_=divisor_cs(i)
    if cnt==9:s+=1
print(s)