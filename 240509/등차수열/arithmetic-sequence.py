n=int(input())
arr=list(map(int,input().split()))

answer=0
for i in range(1,101):
    for j in range(len(arr)-1):
        for k in range(j+1,len(arr)):
            if arr[j]<=i<=arr[k] or arr[k]<=i<=arr[j]:
                if abs(arr[j]-i)==abs(arr[k]-i):
                    answer+=1
print(answer)