n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
cnt=dict()
case_a_b=[]
case_c_d=[]
for i in range(n):
    for j in range(n):
        if a[i]+b[j] in cnt:
            cnt[a[i]+b[j]]+=1
        else:
            cnt[a[i]+b[j]]=1
for i in range(n):
    for j in range(n):
        if c[i]+d[j] in cnt:
            cnt[c[i]+d[j]]+=1
        else:
            cnt[c[i]+d[j]]=1
answer=0
for i in list(set(cnt.keys())):
    if i==100-i:
        if i in cnt:
            answer+=(cnt[i])*(cnt[i]-1)
    else:
        if i in cnt and 100-i in cnt:
            answer+=(cnt[i])*(cnt[100-i])
print(answer//2)