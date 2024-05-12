n=int(input())
arr=[]
for i in range(n):
    name,h,w=map(str,input().split())
    arr.append((name,int(h),int(w)))
arr.sort(key=lambda x:x[1])
for i in range(n):
    print(*arr[i])