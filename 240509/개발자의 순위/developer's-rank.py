k,n=map(int,input().split())
arr=[]
for i in range(k):
    arr.append(list(map(int,input().split())))

answer=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j:
            cnt=0
            for t in range(k):
                if arr[t].index(i)<arr[t].index(j):
                    cnt+=1
            if cnt==k:
                answer+=1
print(answer)