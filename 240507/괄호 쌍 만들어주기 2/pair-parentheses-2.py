s=input()
n=len(s)
answer=0
for i in range(0,n-2):
    if s[i]=='(' and s[i+1]=='(':
        for j in range(i+2,n-1):
            if s[j]==')' and s[j+1]==')':
                answer+=1
print(answer)