n=int(input())
answer=0
while True:
    answer+=n//5
    n%=5
    if n==0:
        break
    answer+=n//2
    n%=2
    if n==0:
        break
print(answer)