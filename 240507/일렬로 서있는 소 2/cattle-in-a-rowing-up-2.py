n=int(input())
arr=list(map(int,input().split()))
answer=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if arr[i]<=arr[j] and arr[j]<=arr[k]:
                answer+=1

print(answer)