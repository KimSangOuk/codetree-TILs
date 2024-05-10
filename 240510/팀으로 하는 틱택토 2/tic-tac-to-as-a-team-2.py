board=[]
for i in range(3):
    board.append(list(input()))
for i in range(3):
    for j in range(3):
        board[i][j]=int(board[i][j])

team=set()
for k in range(3):
    new_set=set(board[k])
    if len(list(new_set))==2:
        arr=list(new_set)
        arr.sort()
        team.add(tuple(arr))
for k in range(3):
    new_set=set()
    for t in range(3):
        new_set.add(board[t][k])
    if len(list(new_set))==2:
        arr=list(new_set)
        arr.sort()
        team.add(tuple(arr))
side1=set([board[0][0],board[1][1],board[2][2]])
if len(list(side1))==2:
    team.add(tuple(list(side1)))
side2=set([board[0][2],board[1][1],board[2][0]])
if len(list(side2))==2:
    team.add(tuple(list(side2)))

print(len(list(team)))