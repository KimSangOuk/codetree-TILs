n,b=map(int,input().split())
students=list()
for i in range(n):
    p,s=map(int,input().split())
    students.append((p,s))

students.sort(key=lambda x:x[0]+x[1])

answer=0
for i in range(n):
    cost=0
    cnt=0
    for j in range(n):
        if i==j:
            cost+=students[j][0]//2+students[j][1]
        else:
            cost+=students[j][0]+students[j][1]
        if cost<=b:
            cnt+=1
    answer=max(answer,cnt)
print(answer)