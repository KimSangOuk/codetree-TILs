n,m=map(int,input().split())

a,b=[0],[0]
a_pos,b_pos=0,0
for i in range(n):
    d,t=input().split()
    for k in range(int(t)):
        if d=='R':
            a_pos+=1
        elif d=='L':
            a_pos-=1
        a.append(a_pos)
for i in range(m):
    d,t=input().split()
    for k in range(int(t)):
        if d=='R':
            b_pos+=1
        elif d=='L':
            b_pos-=1
        b.append(b_pos)
answer=0
for i in range(1,len(a)):
    if a[i]==b[i]:
        answer=i
        break
if answer==0:
    print(-1)
else:
    print(answer)