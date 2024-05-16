n,m=map(int,input().split())
arr=list(map(int,input().split()))
answer=0
last_dist=m*2
for i in range(n):
    # print(i,last_dist,answer)
    if (i==0 and arr[i]==1 and last_dist==m*2) or (arr[i]==1 and last_dist==0):
        answer+=1
        last_dist=m*2
    elif m*2>=last_dist>=0:
        last_dist-=1
    # print(i,last_dist,answer)
print(answer)