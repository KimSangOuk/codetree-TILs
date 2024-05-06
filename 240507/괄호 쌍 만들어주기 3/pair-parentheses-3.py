s=input()

length=len(s)
answer=0
for i in range(length):
    if s[i]=='(':
        for j in range(i+1,length):
            if s[j]==')':
                answer+=1

print(answer)