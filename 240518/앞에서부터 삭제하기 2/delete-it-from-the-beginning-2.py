n=int(input())
arr=list(map(int,input().split()))

answer=0
for i in range(1,n-1):
    tmp=arr[i:]
    tmp.sort()
    answer=max(sum(tmp[1:])/len(tmp[1:]),answer)
print("{:.2f}".format(answer))