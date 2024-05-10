n=int(input())
arr_w=[0]*200001
arr_b=[0]*200001
arr_end=[0]*200001

start=100000
for i in range(n):
    dict,dir=input().split()
    dict=int(dict)
    for j in range(dict):
        if dir=='R':
            arr_b[start+j]+=1
            arr_end[start+j]=1
        else:
            arr_w[start-j]+=1
            arr_end[start-j]=2
    if dir=='R':
        start+=dict-1
    else:
        start-=dict-1

w_cnt=0
b_cnt=0
g_cnt=0
for i in range(200001):
    if arr_b[i]>=2 and arr_w[i]>=2:
        g_cnt+=1
    elif arr_end[i]==1:
        b_cnt+=1
    elif arr_end[i]==2:
        w_cnt+=1

print(w_cnt,b_cnt,g_cnt)