n,g=map(int,input().split())
group=[]
invited=set([1])
for i in range(g):
    arr=list(map(int,input().split()))
    group.append(sorted(arr[1:]))

group.sort(key=lambda x:len(x))
# print(group)
for k in group:
    cnt=0
    for j in k:
        if j in invited:
            cnt+=1
    if cnt==len(k)-1:
        invited=invited|set(k)
# print(invited)
print(len(list(invited)))