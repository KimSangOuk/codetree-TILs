n,m=map(int,input().split())
board=list()

for i in range(n):
    board.append(list(map(int,input().split())))

answer=0
for i in range(n):
    cnt=1
    now=board[i][0]
    for j in range(1,n):
        if now==board[i][j]:
            cnt+=1
        else:
            cnt=1
            now=board[i][j]
        if cnt==m:
            answer+=1

for j in range(n):
    cnt=1
    now=board[0][j]
    for i in range(1,n):
        if now==board[i][j]:
            cnt+=1
        else:
            cnt=1
            now=board[i][j]
        if cnt==m:
            answer+=1

print(answer)