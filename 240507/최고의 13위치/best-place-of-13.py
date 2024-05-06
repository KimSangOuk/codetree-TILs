n=int(input())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

answer=0
for i in range(n):
    for j in range(n):
        if j+2<n:
            answer=max(answer,board[i][j]+board[i][j+1]+board[i][j+2])

print(answer)