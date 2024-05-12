n=int(input())
arr=list(map(int,input().split()))
arr.sort()
a,b=0,0
for i in range(n//2):
    a+=arr[i]+arr[n*2-i-1]
for i in range(n//2,n):
    b+=arr[i]+arr[n*2-i-1]
print(max(a,b))