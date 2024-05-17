n,m=map(int,input().split())
arr=list()
for i in range(2*n):
    arr.append(list(input()))

answer=0
for i in range(m-2):
    for j in range(i+1,m-1):
        for k in range(j+1,m):
            a=set()
            b=set()
            for t in range(n):
                s=arr[t][i]+arr[t][j]+arr[t][k]
                a.add(s)
            for t in range(n,2*n):
                s=arr[t][i]+arr[t][j]+arr[t][k]
                b.add(s)
            tf=True
            for p in list(a):
                if p in b:
                    tf=False
                    break
            if tf:
                answer+=1
print(answer)