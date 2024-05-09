import copy

n,b=map(int,input().split())
students=list()
for i in range(n):
    p,s=map(int,input().split())
    students.append([p,s])



answer=0
for i in range(n):
    cost=0
    cnt=0
    tmp=copy.deepcopy(students)
    tmp[i][0]//=2
    tmp.sort(key=lambda x:x[0]+x[1])
    for j in range(n):
        cost+=tmp[j][0]+tmp[j][1]
        if cost<=b:
            cnt+=1
    tmp[i][0]*=2
    answer=max(answer,cnt)
print(answer)