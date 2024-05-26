n=int(input())

s=list(input())
target=list(input())
cnt=0
start=False
for i in range(n-1,-1,-1):
    if s[i]!=target[i]:
        cnt+=1
        for j in range(i+1):
            if s[j]=='G':
                s[j]='H'
            else:
                s[j]='G'
    # print(s)
print(cnt)