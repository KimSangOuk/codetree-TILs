n=int(input())
s=list(input())
target=list(input())

start=False
term=0
cnt=0
for i in range(n):
    if not start and s[i]!=target[i]:
        start=True
        term+=1
        cnt+=1
    elif start and s[i]!=target[i]:
        term+=1
        if term==4:
            term=0
            start=False
    elif start and s[i]==target[i]:
        start=False
        term=0
    
print(cnt)