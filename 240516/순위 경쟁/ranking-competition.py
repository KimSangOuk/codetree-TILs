n=int(input())
rank=['A','B','C']
name=['A','B','C']
score=[0,0,0]
answer=0
for i in range(n):
    s,c=map(str,input().split())
    if s=='A':
        score[0]+=int(c)
    elif s=='B':
        score[1]+=int(c)
    else:
        score[2]+=int(c)
    new_set=[]
    max_score=-int(1e9)
    for k in range(3):
        if max_score<score[k]:
            max_score=score[k]
            new_set=[name[k]]
        elif max_score==score[k]:
            new_set.append(name[k])
    if new_set!=rank:
        answer+=1
        rank=new_set
print(answer)