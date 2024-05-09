x,y=map(int,input().split())

answer=0
for i in range(x,y+1):
    num=[0]*10
    for s in list(str(i)):
        num[int(s)]+=1
    cnt_1=0
    cnt_left=0
    for j in num:
        if j==1:
            cnt_1+=1
        elif j==len(str(i))-1:
            cnt_left+=1
    if cnt_1==1 and cnt_left==1:
        answer+=1
print(answer)