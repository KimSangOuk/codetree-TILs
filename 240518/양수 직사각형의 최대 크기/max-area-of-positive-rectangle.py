n,m=map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))
answer=0
for i in range(1,n+1):
    for j in range(1,m+1):
        h,w=i,j
        for s in range(n-h+1):
            for t in range(m-w+1):
                tf=True
                for k in range(s,s+h):
                    for q in range(t,t+w):
                        if board[k][q]<=0:
                            tf=False
                            break
                if tf:
                    # if answer<h*w:
                    #     print(h,w,s,t)
                    answer=max(answer,h*w)
if answer==0:
    print(-1)
else:
    print(answer)