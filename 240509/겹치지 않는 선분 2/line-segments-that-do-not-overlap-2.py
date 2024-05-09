n=int(input())

points=[]
for i in range(n):
    x1,x2=map(int,input().split())
    points.append((x1,x2))

answer=0

for i in range(n):
    tf=True
    for j in range(n):
        if i!=j:
            if (points[i][0]<=points[j][0] and points[i][1]>=points[j][1]) or ((points[i][0]>=points[j][0] and points[i][1]<=points[j][1])):
                tf=False
                break
    if tf:
        answer+=1
print(answer)