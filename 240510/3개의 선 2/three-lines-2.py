n=int(input())
points=[]

for i in range(n):
    points.append(tuple(map(int,input().split())))

line=[]

for i in range(n):
    find=False
    for j in range(len(line)):
        if line[j][0]==points[i][0] or line[j][1]==points[i][1]:
            find=True
            break
    if find:
        continue
    for j in range(n):
        if i!=j:
            if points[i][0]==points[j][0]:
                line.append((points[i][0],-1))
                break
            elif points[j][1]==points[i][1]:
                line.append((-1,points[i][1]))
                break

if len(line)>3:
    print(0)
else:
    print(1)