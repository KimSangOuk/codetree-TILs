n=int(input())
board=[[0]*201 for _ in range(201)]

for i in range(n):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            if i%2==0:
                board[j][k]=1
            else:
                board[j][k]=2

answer=0
for i in range(201):
    for j in range(201):
        if board[i][j]==2:
            answer+=1
print(answer)