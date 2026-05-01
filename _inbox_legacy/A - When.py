K=int(input())
if K<60:print(str(21)+":"+str(K).zfill(2))
else:print(str(22)+":"+str(K-60).zfill(2))