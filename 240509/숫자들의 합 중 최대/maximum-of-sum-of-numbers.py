x,y=map(int,input().split())

answer=0
for i in range(x,y+1):
    answer=max(answer,sum(list(map(int,list(str(i))))))
print(answer)