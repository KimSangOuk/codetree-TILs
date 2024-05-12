n,m=map(int,input().split())
a,b=[0],[0]
a_pos,b_pos=0,0
for i in range(n):
    v,t=map(int,input().split())
    for j in range(t):
        a_pos+=v
        a.append(a_pos)
for i in range(m):
    v,t=map(int,input().split())
    for j in range(t):
        b_pos+=v
        b.append(b_pos)

answer=0
for i in range(2,len(a)):
    if a[i]>b[i] and a[i-1]<=b[i-1]:
        answer+=1
    elif a[i]<b[i] and a[i-1]>=b[i-1]:
        answer+=1
print(answer)