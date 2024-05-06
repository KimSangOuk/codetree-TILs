n=int(input())
points=list()
for i in range(n):
    points.append(tuple(map(int,input().split())))

answer=int(1e9)
for i in range(1,n-1):
    pass_num=i
    sum_value=0
    prev=0
    for j in range(1,n):
        if j==pass_num:
            continue
        sum_value+=(abs(points[j][0]-points[prev][0])+abs(points[prev][1]-points[j][1]))
        prev=j
    answer=min(answer,sum_value)

print(answer)