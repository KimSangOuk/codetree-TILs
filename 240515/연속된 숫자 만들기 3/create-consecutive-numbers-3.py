a,b,c=map(int,input().split())
arr=[a,b,c]
arr.sort()
dist=max(b-a,c-b)
print(dist-1)