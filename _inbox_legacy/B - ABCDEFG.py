p, _, q = list(input())
p = p.replace("A", "0").replace("B", "3").replace("C", "4").replace("D", "8").replace("E", "9").replace("F", "14").replace("G", "23")
q = q.replace("A", "0").replace("B", "3").replace("C", "4").replace("D", "8").replace("E", "9").replace("F", "14").replace("G", "23")

print(abs(int(p) - int(q)))