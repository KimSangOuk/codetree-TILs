a,b=map(int,input().split())
k=list(input())
n=0
for i in range(len(k)):
    n=n*a+int(k[i])

answer=""
while True:
    if b>n:
        answer=str(n)+answer
        break
    answer=str(n%b)+answer
    n//=b
print(answer)