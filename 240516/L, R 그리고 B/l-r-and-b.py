from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]

board=[]
l_pos,b_pos,r_pos=0,0,0
for i in range(10):
    arr=list(input())
    for j in range(10):
        if arr[j]=='L':
            l_pos=(i,j)
        elif arr[j]=='R':
            r_pos=(i,j)
        elif arr[j]=='B':
            b_pos=(i,j)
    board.append(arr)
q=deque()
visited=[[-1]*10 for _ in range(10)]
visited[l_pos[0]][l_pos[1]]=0
q.append(l_pos)
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=10 or ny>=10:
            continue
        if visited[nx][ny]!=-1:
            continue
        if board[nx][ny]=='R':
            continue
        visited[nx][ny]=visited[x][y]+1
        q.append((nx,ny))
print(visited[b_pos[0]][b_pos[1]]-1)