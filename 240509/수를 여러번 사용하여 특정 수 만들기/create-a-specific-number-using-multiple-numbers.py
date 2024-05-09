a,b,c=map(int,input().split())

answer=0
for i in range(1001):
    for j in range(1001):
        if a*i+b*j<=c:
            answer=max(a*i+b*j,answer)
print(answer)