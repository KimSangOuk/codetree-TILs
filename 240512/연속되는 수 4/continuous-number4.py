n=int(input())
arr=list()
for i in range(n):
    arr.append(int(input()))

answer=1
cnt=0
for i in range(n):
    if i==0 or arr[i]<=arr[i-1]:
        cnt=1
    else:
        cnt+=1
        answer=max(answer,cnt)
print(answer)