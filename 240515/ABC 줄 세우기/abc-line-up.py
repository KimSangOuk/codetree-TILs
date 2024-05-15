n=int(input())
arr=list(map(str,input().split()))
cnt=0
for i in range(n):
    if ord(arr[i])==ord('A')+i:
        cnt+=1
if cnt==n:
    print(0)
else:
    print(n-cnt-1)