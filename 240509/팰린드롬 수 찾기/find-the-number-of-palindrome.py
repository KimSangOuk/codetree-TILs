x,y=map(int,input().split())
answer=0
for i in range(x,y+1):
    if len(str(i))%2==0:
        if str(i)[0:len(str(i))//2]==str(i)[len(str(i))//2:][::-1]:
            answer+=1
    else:
        if str(i)[0:len(str(i))//2]==str(i)[len(str(i))//2+1:][::-1]:
            answer+=1
print(answer)