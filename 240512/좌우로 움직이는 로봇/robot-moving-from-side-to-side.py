n,m=map(int,input().split())
a_pos,b_pos=0,0
a,b=[0],[0]

for i in range(n):
    t,d=input().split()
    for j in range(int(t)):
        if d=='R':
            a_pos+=1
        elif d=='L':
            a_pos-=1
        a.append(a_pos)
for i in range(m):
    t,d=input().split()
    for j in range(int(t)):
        if d=='R':
            b_pos+=1
        elif d=='L':
            b_pos-=1
        b.append(b_pos)
answer=0
if len(a)>len(b):
    b+=[b[len(b)-1]]*(len(a)-len(b))
else:
    a+=[a[len(a)-1]]*(len(b)-len(a))

for i in range(2,max(len(a),len(b))):
    if a[i-1]!=b[i-1] and a[i]==b[i]:
        answer+=1
print(answer)