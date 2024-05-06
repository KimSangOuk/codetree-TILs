r,c=map(int,input().split())
board=[]
for i in range(r):
    board.append(list(map(str,input().split())))

now=board[0][0]

answer=0
for i in range(1,r):
    for j in range(1,c):
        if board[i][j]!=now:
            for k in range(i+1,r-1):
                for t in range(j+1,c-1):
                    if board[k][t]==now:
                        answer+=1

print(answer)