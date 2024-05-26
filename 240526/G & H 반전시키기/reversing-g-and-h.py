n=int(input())
s=list(input())
target=list(input())
start=False
cnt=0
for i in range(len(s)):
    if not start and s[i]!=target[i]:
        start=True
        cnt+=1
    elif start and s[i]==target[i]:
        start=False
print(cnt)