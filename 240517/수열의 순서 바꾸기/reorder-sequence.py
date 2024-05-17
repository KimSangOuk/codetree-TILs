n=int(input())
arr=list(map(int,input().split()))

answer=-1
for i in range(1):
    tmp=sorted(arr[i:])
    if tmp==arr[i:]:
        answer=i
        break
print(answer)