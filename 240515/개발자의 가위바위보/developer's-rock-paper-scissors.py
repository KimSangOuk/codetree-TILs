n=int(input())

games=[]

for i in range(n):
    a,b=map(int,input().split())
    games.append((a,b))

answer=0
# 1 가위 2 바위 3 보
cnt=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==3:
        cnt+=1
    elif games[i][0]==2 and games[i][1]==1:
        cnt+=1
    elif games[i][0]==3 and games[i][1]==2:
        cnt+=1
answer=max(cnt,answer)
# 1 가위 2 보 3 바위
cnt=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==2:
        cnt+=1
    elif games[i][0]==2 and games[i][1]==3:
        cnt+=1
    elif games[i][0]==3 and games[i][1]==1:
        cnt+=1
answer=max(cnt,answer)
# 1 바위 2 보 3 가위
cnt=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==3:
        cnt+=1
    elif games[i][0]==2 and games[i][1]==1:
        cnt+=1
    elif games[i][0]==3 and games[i][1]==2:
        cnt+=1
answer=max(cnt,answer)
# 1 바위 2 가위 3 보
cnt=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==2:
        cnt+=1
    elif games[i][0]==2 and games[i][1]==3:
        cnt+=1
    elif games[i][0]==3 and games[i][1]==1:
        cnt+=1
answer=max(cnt,answer)
# 1 보 2 가위 3 바위
cnt=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==3:
        cnt+=1
    elif games[i][0]==2 and games[i][1]==1:
        cnt+=1
    elif games[i][0]==3 and games[i][1]==2:
        cnt+=1
answer=max(cnt,answer)
# 1 보 2 바위 3 가위
cnt=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==2:
        cnt+=1
    elif games[i][0]==2 and games[i][1]==3:
        cnt+=1
    elif games[i][0]==3 and games[i][1]==1:
        cnt+=1
answer=max(cnt,answer)
print(answer)