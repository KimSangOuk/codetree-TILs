import copy

n=int(input())
tmp=list(map(int,input().split()))
arr=[]
for i in range(1,n+1):
    arr.append((i,tmp[i-1]))

new_arr=[]
k=sorted(tmp)
for i in range(1,n+1):
    new_arr.append((i,k[i-1]))
new_arr.sort(key=lambda x:x[1])

used=[False]*(n+1)
for i in range(n):
    for j in range(n):
        if arr[i][1]==new_arr[j][1] and not used[new_arr[j][0]]:
            used[new_arr[j][0]]=True
            print(j+1,end=' ')
            break