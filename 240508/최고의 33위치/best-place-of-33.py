n=int(input())

board=list()
for i in range(n):
    board.append(list(map(int,input().split())))

answer=0

for i in range(n-2):
    for j in range(n-2):
        coins_cnt=0
        for a in range(3):
            for b in range(3):
                coins_cnt+=board[i+a][j+b]
        answer=max(coins_cnt,answer)
print(answer)