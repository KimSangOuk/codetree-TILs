n,k,p,t=map(int,input().split())
get_cold=[0]*(n+1)
cnt_put=[k]*(n+1)
record=list()
for i in range(t):
    record.append(list(map(int,input().split())))
get_cold[p]=1
record.sort()
for i in range(t):
    if get_cold[record[i][1]]==1 and get_cold[record[i][2]]==1:
        if cnt_put[record[i][1]]>0:
            cnt_put[record[i][1]]-=1
        if cnt_put[record[i][2]]>0:
            cnt_put[record[i][2]]-=1
    elif get_cold[record[i][1]]==1:
        if cnt_put[record[i][1]]>0:
            cnt_put[record[i][1]]-=1
            get_cold[record[i][2]]=1
    elif get_cold[record[i][2]]==1:
        if cnt_put[record[i][2]]>0:
            cnt_put[record[i][2]]-=1
            get_cold[record[i][1]]=1

for i in range(1,n+1):
    print(get_cold[i],end='')