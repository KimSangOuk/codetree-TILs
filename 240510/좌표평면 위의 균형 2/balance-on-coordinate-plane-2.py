n=int(input())
points=[]
for i in range(n):
    points.append(tuple(map(int,input().split())))

answer=int(1e9)
for x in range(2,99,2):
    for y in range(2,99,2):
        points_num=[0,0,0,0]
        for i in range(n):
            if x<points[i][0] and y<points[i][1]:
                points_num[0]+=1
            elif x>points[i][0] and y<points[i][1]:
                points_num[1]+=1
            elif x>points[i][0] and y>points[i][1]:
                points_num[2]+=1
            else:
                points_num[3]+=1
        answer=min(answer,max(points_num))
print(answer)