list = [ i for i in range(100) ]

for a in list:
    b = 100 - a
    s = (105 * a)//100 + (105 * b)//100
    if s == 105: print(f"a,bの値が{a,b}のときにf(a,b)の値は{(1.08 * a)/1.00 + (1.08 * b)/1.00}")
