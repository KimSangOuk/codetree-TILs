n=int(input())
arr=[0]*200001
start=100000

for i in range(n):
    dict,dir=input().split()
    dict=int(dict)
    for j in range(dict):
        if dir=='R':
            arr[start+j]=1
        elif dir=='L':
            arr[start-j]=2
    if dir=='R':
        start+=dict-1
    else:
        start-=dict-1

w_cnt=0
b_cnt=0
for i in range(200001):
    if arr[i]==1:
        b_cnt+=1
    elif arr[i]==2:
        w_cnt+=1

print(w_cnt,b_cnt)