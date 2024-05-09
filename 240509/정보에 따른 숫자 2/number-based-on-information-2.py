t,a,b=map(int,input().split())
arr=list()
for i in range(t):
    alpha,pos=input().split()
    arr.append((alpha,int(pos)))

arr.sort(key=lambda x:x[1])

answer=0
for i in range(a,b+1):
    d1,d2=int(1e9),int(1e9)
    for alpha,pos in arr:
        if alpha=='S':
            d1=min(d1,abs(i-pos))
        if alpha=='N':
            d2=min(d2,abs(i-pos))
    if d1<=d2:
        answer+=1
print(answer)