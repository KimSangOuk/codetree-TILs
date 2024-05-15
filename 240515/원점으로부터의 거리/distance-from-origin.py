n=int(input())
points=[]
for i in range(1,n+1):
    x,y=map(int,input().split())
    points.append((i,x,y))

points.sort(key=lambda x:abs(x[1])+abs(x[2]))

for i in range(n):
    print(points[i][0])