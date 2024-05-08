n,m=map(int,input().split())

arr_a=list(map(int,input().split()))
arr_b=list(map(int,input().split()))
arr_b.sort()

answer=0
for i in range(n-m+1):
    arr=arr_a[i:i+m]
    arr.sort()

    if arr==arr_b:
        answer+=1

print(answer)