n=int(input())
bombs=[]
for i in range(n):
    score,t=map(int,input().split())
    bombs.append((score,t))
bombs.sort(key=lambda x:(x[1],-x[0]))
already=0
answer=0
# print(bombs)
for i in range(n):
    score,t=bombs[i]
    if already==t:
        continue
    else:
        answer+=score
        already=t
print(answer)