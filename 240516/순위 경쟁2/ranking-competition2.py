n=int(input())
rank=['A','B']
score=[0,0]
answer=0
for i in range(n):
    s,c=map(str,input().split())
    if s=='A':
        score[0]+=int(c)
    else:
        score[1]+=int(c)
    new_set=[]
    if score[0]==score[1]:
        new_set=['A','B']
    elif score[0]>score[1]:
        new_set=['A']
    else:
        new_set=['B']
    if new_set!=rank:
        answer+=1
        rank=new_set
print(answer)