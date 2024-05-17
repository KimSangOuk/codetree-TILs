n,g=map(int,input().split())
group=[]
invited=set([1])
for i in range(g):
    arr=list(map(int,input().split()))
    group.append(sorted(arr[1:]))

group.sort()
for k in group:
    for j in k:
        if j not in invited:
            invited.add(j)
            break
print(len(list(invited)))