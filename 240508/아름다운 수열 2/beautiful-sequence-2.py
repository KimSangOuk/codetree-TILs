n,m=map(int,input().split())

arr_a=list(map(int,input().split()))
arr_b=set(list(map(int,input().split())))

answer=0
for i in range(n-m+1):
    tf=True
    for k in arr_a[i:i+m]:
        if k not in arr_b:
            tf=False
    if tf:
        answer+=1

print(answer)