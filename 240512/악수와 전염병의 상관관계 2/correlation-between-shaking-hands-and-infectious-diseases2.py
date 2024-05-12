n,k,p,t=map(int,input().split())
get_cold=[0]*(n+1)
record=list()
for i in range(t):
    record.append(list(map(int,input().split())))
get_cold[p]=1
record.sort()
for i in range(t):
    if p>0 and (get_cold[record[i][1]]==1 or get_cold[record[i][2]]==1):
        p-=1
        get_cold[record[i][1]]=1
        get_cold[record[i][2]]=1

for i in range(1,n+1):
    print(get_cold[i],end='')