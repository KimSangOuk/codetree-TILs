n=int(input())
arr=list(map(int,input().split()))
yang=[]
eum=[]
for i in range(n):
    if arr[i]>0:
        yang.append(arr[i])
    elif arr[i]<0:
        eum.append(arr[i])
yang.sort(reverse=True)
eum.sort()
answer=max(yang[0]*yang[1]*yang[2],eum[0]*eum[1]*yang[0])
print(answer)