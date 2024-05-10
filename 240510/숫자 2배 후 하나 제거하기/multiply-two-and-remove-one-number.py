n=int(input())
arr=list(map(int,input().split()))

answer=int(1e9)
for i in range(n):
    arr[i]*=2
    for j in range(n):
        remain_arr=[]
        for k in range(n):
            if k!=j:
                remain_arr.append(arr[k])
        sum_value=0
        for k in range(n-2):
            sum_value+=abs(remain_arr[k]-remain_arr[k+1])
        answer=min(answer,sum_value)
    arr[i]//=2
print(answer)