n=int(input())
points=[]
for i in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

answer=int(2e9)
for i in range(n):
    max_x,max_y=0,0
    min_x,min_y=40000,40000
    for j in range(n):
        if i!=j:
            max_x=max(points[j][0],max_x)
            max_y=max(points[j][1],max_y)
            min_x=min(points[j][0],min_x)
            min_y=min(points[j][1],min_y)

    answer=min(answer,(max_x-min_x)*(max_y-min_y))
print(answer)