while True:
    n = int(input())
    if n == 0:break
    s = input()

    strings = s
    
    c = 0

    for i in range(n):
        if s[i] == s[n-i-1]: c+=1
        else: break
    
    output = strings+s[c:]

    if output == s: output+=s[0]

    print(output)
