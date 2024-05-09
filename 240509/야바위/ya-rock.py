n=int(input())
steps=list()
for i in range(n):
    steps.append(list(map(int,input().split())))

answer=0
for i in range(1,4):
    check=i
    arr=[False]*4
    arr[check]=True
    score=0
    for a,b,c in steps:
        arr[a],arr[b]=arr[b],arr[a]
        if arr[c]:
            score+=1
    answer=max(answer,score)
print(answer)