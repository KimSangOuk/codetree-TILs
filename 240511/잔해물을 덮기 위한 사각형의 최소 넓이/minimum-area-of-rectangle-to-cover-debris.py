board=[[0]*2001 for _ in range(2001)]
x1,y1,x2,y2=map(int,input().split())
for i in range(x1+1000,x2+1000):
    for j in range(y1+1000,y2+1000):
        board[i][j]=1
x1,y1,x2,y2=map(int,input().split())
for i in range(x1+1000,x2+1000):
    for j in range(y1+1000,y2+1000):
        board[i][j]=0
min_x,min_y,max_x,max_y=2001,2001,-1,-1
for i in range(2001):
    for j in range(2001):
        if board[i][j]==1:
            min_x=min(min_x,i)
            max_x=max(max_x,i)
            min_y=min(min_y,j)
            max_y=max(max_y,j)
for i in range(min_x,max_x+1):
    for j in range(min_y,max_y+1):
        board[i][j]=1
answer=0
for i in range(2001):
    for j in range(2001):
        if board[i][j]==1:
            answer+=1
print(answer)