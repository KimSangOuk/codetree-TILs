n=int(input())
points=[]

for i in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

answer=0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            x1,y1=points[i]
            x2,y2=points[j]
            x3,y3=points[k]
            if x1==x2 or x2==x3 or x1==x3:
                if y1==y2 or y2==y3 or y1==y3:
                    answer=max(answer,abs((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)))

print(answer)