n=int(input())
points=[]

for i in range(n):
    points.append(tuple(map(int,input().split())))

x_set=set()
y_set=set()
for i in range(n):
    x_set.add(points[i][0])
    y_set.add(points[i][1])

line=[]
for i in x_set:
    line.append((i,-1))
for i in y_set:
    line.append((-1,i))

answer=0
length=len(line)
for i in range(length-2):
    for j in range(i+1,length-1):
        for k in range(j+1,length):
            tf=True
            for a,b in points:
                if (line[i][0]==a or line[i][1]==b) or (line[j][0]==a or line[j][1]==b) or (line[k][0]==a or line[k][1]==b):
                    continue
                else:
                    tf=False
            if tf:
                answer=1
print(answer)