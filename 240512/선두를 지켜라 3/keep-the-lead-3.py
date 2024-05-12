a,b=[0],[0]
a_pos,b_pos=0,0
n,m=map(int,input().split())
for i in range(n):
    v,t=map(int,input().split())
    for j in range(t):
        a_pos+=v
        a.append(a_pos)
for j in range(m):
    v,t=map(int,input().split())
    for j in range(t):
        b_pos+=v
        b.append(b_pos)

answer=0
now=set()
for i in range(1,len(a)):
    first_group_set=set()
    if a[i]==b[i]:
        first_group_set=[a,b]
    elif a[i]>b[i]:
        first_group_set=[a]
    else:
        first_group_set=[b]
    if first_group_set!=now:
        answer+=1
    now=first_group_set
print(answer)