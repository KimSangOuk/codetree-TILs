n,m=map(int,input().split())

board=[]
for i in range(n):
    board.append(list(map(int,input().split())))

answer=0
for h in range(1,n+1):
    for w in range(1,m+1):
        all_positive=True
        for x in range(n-h+1):
            for y in range(m-w+1):
                if board[x][y]<=0:
                    all_positive=False
                    break
        if all_positive:
            answer=max(answer,h*w)
print(answer)