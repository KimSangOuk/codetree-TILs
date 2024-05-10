n=int(input())
s=input()

answer=int(1e9)
for i in range(1,n+1):
    tf=True
    for start_index in range(n-i+1):
        # print(s[start_index:start_index+i])
        if s[start_index:start_index+i] in s[start_index+1:]:
            tf=False
            break
    if tf:
        answer=min(answer,i)
print(answer)