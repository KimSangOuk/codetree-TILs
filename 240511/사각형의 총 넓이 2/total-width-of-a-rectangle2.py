board=[[0]*201 for _ in range(201)]
n=int(input())
for i in range(n):
    x1,y1,x2,y2=map(int,input().split())
    x1,y1,x2,y2=x1+100,y1+100,x2+100,y2+100
    for j in range(x1,x2):
        for k in range(y1,y2):
            board[j][k]=1

answer=0
for i in range(201):
    answer+=sum(board[i])
print(answer)