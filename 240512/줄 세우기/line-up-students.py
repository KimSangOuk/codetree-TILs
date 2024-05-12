n=int(input())
arr=list()
for i in range(1,n+1):
    h,w=map(int,input().split())
    arr.append((h,w,i))

arr.sort(key=lambda x:(-x[0],-x[1],x[2]))
for i in range(n):
    print(*arr[i])