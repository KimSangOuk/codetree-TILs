n=int(input())
arr=list()
for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))

answer=0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            tf=True
            line=[0]*101
            for t in range(n):
                if t==i or t==j or t==k:
                    continue
                for c in range(arr[t][0],arr[t][1]+1):
                    line[c]+=1
            for t in range(101):
                if line[t]>1:
                    tf=False
                    break
            if tf:
                answer+=1
print(answer)