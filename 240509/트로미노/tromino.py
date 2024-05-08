n,m=map(int,input().split())
board=list()
for i in range(n):
    board.append(list(map(int,input().split())))

answer=0

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dfs(deep,x,y,visited,v):
    global answer
    if x<0 or y<0 or x>=n or y>=m or visited[x][y]:
        return
    if deep==3:
        v+=board[x][y]
        answer=max(answer,v)
        # print("깊이3",x,y,v)
    else:
        for i in range(4):
            # print("자 드간다",x,y)
            visited[x][y]=True
            dfs(deep+1,x+dx[i],y+dy[i],visited,v+board[x][y])

for i in range(n):
    for j in range(m):
        visited=[[False]*m for i in range(n)]
        dfs(1,i,j,visited,0)

print(answer)