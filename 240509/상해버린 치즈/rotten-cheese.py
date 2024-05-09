n,m,d,s=map(int,input().split())
eat_data=[]
sick_data=[]
cheeses=dict()
for i in range(m):
    cheeses[i]=[]
for i in range(d):
    eat_data.append(tuple(map(int,input().split())))
for i in range(s):
    sick_data.append(tuple(map(int,input().split())))

for i in range(s):
    p,t=sick_data[i]
    for j in range(d):
        ep,em,et=eat_data[j]
        if ep==p and et<t:
            cheeses[em-1].append(ep)

sick_check=[0]*n
for i in range(m):
    if len(set(cheeses[i]))==s:
        for j in range(d):
            ep,em,et=eat_data[j]
            if em==i+1:
                sick_check[ep-1]=1

answer=sum(sick_check)
print(answer)