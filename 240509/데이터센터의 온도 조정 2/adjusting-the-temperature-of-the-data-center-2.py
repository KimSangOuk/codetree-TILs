n,c,g,h=map(int,input().split())
arr=list()
for i in range(n):
    ta,tb=map(int,input().split())
    arr.append((ta,tb))

def get_w(array,n,t):
    ta,tb=array[n]
    if t<ta:
        return c
    elif ta<=t<=tb:
        return g
    else:
        return h

answer=0
for t in range(1001):
    total=0
    for i in range(n):
        total+=get_w(arr,i,t)
    answer=max(total,answer)
print(answer)