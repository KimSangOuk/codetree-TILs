n,m=map(int,input().split())
board=list()

for i in range(n):
    board.append(list(map(int,input().split())))

answer=0
arr=[]
for i in range(n):
    arr.append(board[i])

for j in range(n):
    tmp=[]
    for i in range(n):
        tmp.append(board[i][j])
    arr.append(tmp)
    
for k in arr:
    if m==1 and len(k)==1:
        answer+=1
        continue
    cnt=1
    now=k[0]
    for t in range(1,len(k)):
        if k[t]==now:
            cnt+=1
        else:
            cnt=1
            now=k[t]
        if cnt==m:
            answer+=1
            break
print(answer)