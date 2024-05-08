n=int(input())
points=[]

for i in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

answer=int(1e9)
for i in range(n-1):
    for j in range(i+1,n):
        answer=min(answer,(points[i][0]-points[j][0])*(points[i][0]-points[j][0])+(points[i][1]-points[j][1])*(points[i][1]-points[j][1]))
print(answer)