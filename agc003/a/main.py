s = input()
a = []
a.append("N" in s)
a.append("W" in s)
a.append("S" in s)
a.append("E" in s)
print("NYoe s"[(a[0]==a[2] and a[1]==a[3])::2]) 
