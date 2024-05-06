s=list(input())
length=len(s)
answer=0
find=False
for i in range(length):
    if s[i]=='0':
        s[i]='1'
        find=True
        break
if not find:
    s[length-1]='0'
answer=int("0b"+''.join(s),2)
print(answer)