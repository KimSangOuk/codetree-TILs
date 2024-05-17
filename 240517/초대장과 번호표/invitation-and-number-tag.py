n,g=map(int,input().split())
groups=[]
invited=set([1])
for i in range(g):
    arr=list(map(int,input().split()))
    groups.append(sorted(arr[1:]))

find=True
while find:
    find=False
    remove_num=[]
    for i in range(len(groups)):
        cnt=0
        for k in groups[i]:
            if k in invited:
                cnt+=1
        if cnt==len(groups[i])-1:
            invited=invited|set(groups[i])
            find=True
            remove_num.append(i)
    for i in remove_num[::-1]:
        groups.remove(groups[i])
print(len(list(invited)))