h,w=map(int,input().split())
a=[element for row in[list(map(int,input().split()))for _ in range(h)]for element in row]
print(sum(a)-h*w*min(a))