from collections import deque

n,m=map(int,input().split())
board=list()

coins_cnt=0
for i in range(n):
    arr=list(map(int,input().split()))
    board.append(arr)
    for j in range(n):
        if arr[j]==1:
            coins_cnt+=1

max_k=0
for i in range(n):
    if i*i+(i+1)*(i+1)<m*coins_cnt:
        max_k=i
    else:
        break

dx=[0,0,-1,1]
dy=[1,-1,0,0]

answer=0

def bfs(board,x,y,dist):
    q=deque()
    visited=[[-1]*n for _ in range(n)]
    q.append((x,y))
    visited[x][y]=0
    cnt=board[x][y]
    while q:
        n_x,n_y=q.popleft()
        if visited[n_x][n_y]>=dist:
            break
        for i in range(4):
            nx=n_x+dx[i]
            ny=n_y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if visited[nx][ny]!=-1:
                continue
            visited[nx][ny]=visited[n_x][n_y]+1
            q.append((nx,ny))
            cnt+=board[nx][ny]
    return cnt

for i in range(n):
    for j in range(n):
        for k in range(2*n):
            cnt=bfs(board,i,j,k)
            if k*k+(k+1)*(k+1)<=m*cnt:
                answer=max(cnt,answer)

print(answer)