n,m=map(int,input().split())
board=[]
for i in range(n):
    board.append(list(input()))

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

answer=0

for i in range(n):
    for j in range(m):
        x,y=i,j
        for d in range(8):
            new_s=""
            for k in range(3):
                nx=x+dx[d]*k
                ny=y+dy[d]*k
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    break
                new_s+=board[nx][ny]
                # print(new_s)
            if len(new_s)==3 and new_s=='LEE':
                answer+=1

print(answer)