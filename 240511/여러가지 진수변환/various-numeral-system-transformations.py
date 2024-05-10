n,b=map(int,input().split())

answer=""
while True:
    if n<b:
        answer=str(n)+answer
        break
    answer=str(n%b)+answer
    n//=b

print(answer)