board=list()
for i in range(19):
    board.append(list(map(int,input().split())))

answer=0
mid_pos_x=0
mid_pos_y=0
for i in range(19-4):
    for j in range(19-4):
        if board[i][j]==1 and board[i][j+1]==1 and board[i][j+2]==1 and board[i][j+3]==1 and board[i][j+4]==1:
            answer=1
            mid_pos_x,mid_pos_y=i+1,j+3
            break
        elif board[i][j]==1 and board[i+1][j]==1 and board[i+2][j]==1 and board[i+3][j]==1 and board[i+4][j]==1:
            answer=1
            mid_pos_x,mid_pos_y=i+3,j+1
            break
        elif board[i][j]==1 and board[i+1][j+1]==1 and board[i+2][j+2]==1 and board[i+3][j+3]==1 and board[i+4][j+4]==1:
            answer=1
            mid_pos_x,mid_pos_y=i+3,j+3
            break
        elif board[i+4][j]==1 and board[i+3][j+1]==1 and board[i+2][j+2]==1 and board[i+1][j+3]==1 and board[i][j+4]==1:
            answer=1
            mid_pos_x,mid_pos_y=i+3,j+3
            break
        elif board[i][j]==2 and board[i][j+1]==2 and board[i][j+2]==2 and board[i][j+3]==2 and board[i][j+4]==2:
            answer=2
            mid_pos_x,mid_pos_y=i+1,j+3
            break
        elif board[i][j]==2 and board[i+1][j]==2 and board[i+2][j]==2 and board[i+3][j]==2 and board[i+4][j]==2:
            answer=2
            mid_pos_x,mid_pos_y=i+3,j+1
            break
        elif board[i][j]==2 and board[i+1][j+1]==2 and board[i+2][j+2]==2 and board[i+3][j+3]==2 and board[i+4][j+4]==2:
            answer=2
            mid_pos_x,mid_pos_y=i+3,j+3
            break
        elif board[i+4][j]==2 and board[i+3][j+1]==2 and board[i+2][j+2]==2 and board[i+1][j+3]==2 and board[i][j+4]==2:
            answer=2
            mid_pos_x,mid_pos_y=i+3,j+3
            break
    if answer!=0:
        break

print(answer)
if answer!=0:
    print(mid_pos_x,mid_pos_y)