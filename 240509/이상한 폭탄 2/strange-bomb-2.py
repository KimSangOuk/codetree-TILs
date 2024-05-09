n,k=map(int,input().split())

arr=list()
for i in range(n):
    arr.append(int(input()))

answer=0
for i in range(n):
    if arr[i] in arr[i+1:i+k+1]:
        answer=max(answer,arr[i])
if answer==0:
    print(-1)
else:
    print(answer)