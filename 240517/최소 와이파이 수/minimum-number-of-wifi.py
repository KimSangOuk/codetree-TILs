n,m=map(int,input().split())
arr=list(map(int,input().split()))
answer=0
last_cnt=1+m*2
for i in range(n):
    # print(i,last_dist,answer)
    if i==0 and arr[i]==1 and last_cnt==m*2+1:
        last_cnt-=1
        answer+=1
    elif arr[i]==1 and last_cnt==0:
        answer+=1
        last_cnt=m*2
    elif m*2+1>=last_cnt>0:
        last_cnt-=1
    # print(i,last_cnt,answer)
print(answer)