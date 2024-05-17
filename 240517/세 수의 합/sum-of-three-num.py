n,k=map(int,input().split())
cnt=dict()
arr=list(map(int,input().split()))
for i in range(n):
    if arr[i] not in cnt:
        cnt[arr[i]]=1
    else:
        cnt[arr[i]]+=1
answer=0
possible_set=set()
for i in list(set(cnt.keys())):
    last=k-i
    if k-i==i:
        if cnt[i]>=3:
            possible_set.add((i,i,i))
    else:
        for j in list(set(cnt.keys())):
            if i!=j:
                if last-j==j:
                    if j in cnt:
                        possible_set.add(tuple(sorted([i,i,j])))
                else:
                    if j in cnt and last-j in cnt:
                        possible_set.add(tuple(sorted([i,j,last-j])))

for a,b,c in list(possible_set):
    if a==b and b==c:
        answer+=cnt[a]*(cnt[a]-1)*(cnt[a]-2)//6
    elif a==b:
        answer+=(cnt[a]*(cnt[a]-1))//2*cnt[c]
    elif b==c:
        answer+=(cnt[b]*(cnt[b]-1))//2*cnt[a]
    else:
        answer+=cnt[a]*cnt[b]*cnt[c]
print(answer)