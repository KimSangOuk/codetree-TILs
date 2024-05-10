n=int(input())
board=[[0]*201 for _ in range(201)]
for i in range(n):
    a,b=map(int,input().split())
    a,b=a+100,b+100
    for j in range(a,a+8):
        for k in range(b,b+8):
            board[j][k]=1
answer=0
for i in range(201):
    answer+=sum(board[i])
print(answer)