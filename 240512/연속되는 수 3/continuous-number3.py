n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

cnt=0
answer=1
for i in range(n):
    if i==0 or (arr[i-1]>0 and arr[i]<0) or (arr[i-1]<0 and arr[i]>0):
        cnt=1
    else:
        cnt+=1
        answer=max(answer,cnt)
print(answer)