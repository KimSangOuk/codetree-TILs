board=[[0]*2001 for _ in range(2001)]
x1,y1,x2,y2=map(int,input().split())
for i in range(x1,x2):
    for j in range(y1,y2):
        board[i][j]=1
x1,y1,x2,y2=map(int,input().split())
for i in range(x1,x2):
    for j in range(y1,y2):
        board[i][j]=1
x1,y1,x2,y2=map(int,input().split())
for i in range(x1,x2):
    for j in range(y1,y2):
        board[i][j]=2
answer=0
for i in range(2001):
    for j in range(2001):
        if board[i][j]==1:
            answer+=1
print(answer)