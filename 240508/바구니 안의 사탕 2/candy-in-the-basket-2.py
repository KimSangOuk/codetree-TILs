n,k=map(int,input().split())
arr=[0]*101

for i in range(n):
    candy,basket=map(int,input().split())
    arr[basket]+=candy

answer=0
for i in range(0,101):
    c=i
    value=0
    for j in range(c-k,c+k+1):
        if 0<=j<101:
            value+=arr[j]
    answer=max(answer,value)
            

print(answer)