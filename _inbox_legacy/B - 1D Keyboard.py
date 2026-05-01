s = input()
c = 0
for i in range(25):
    c+=abs(s.find(chr(65+i))-s.find(chr(66+i)))
print(c)