import math

n=int(input())
arr=list(map(int,input().split()))

answer=0
for i in range(n):
    for j in range(i,n):
        if sum(arr[i:j+1])/(j+1-i) in arr[i:j+1]:
            answer+=1

print(answer)