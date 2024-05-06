n=int(input())
board=[]
for i in range(n):
     board.append(list(map(int,input().split())))
    
answer=0
for i in range(n):
    for j in range(n-2):
        for k in range(n):
            if k==i:
                for t in range(j+3,n-2):
                    sum_value=0
                    sum_value+=board[i][j]+board[i][j+1]+board[i][j+2]+board[k][t]+board[k][t+1]+board[k][t+2]
                    answer=max(sum_value,answer)
            else:
                for t in range(n-2):
                    sum_value=0
                    sum_value+=board[i][j]+board[i][j+1]+board[i][j+2]+board[k][t]+board[k][t+1]+board[k][t+2]
                    answer=max(sum_value,answer)

print(answer)