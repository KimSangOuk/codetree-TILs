n=int(input())
cnt=dict()
for i in range(n):
    s=input()
    if s not in cnt:
        cnt[s]=1
    else:
        cnt[s]+=1
print(max(cnt.values()))