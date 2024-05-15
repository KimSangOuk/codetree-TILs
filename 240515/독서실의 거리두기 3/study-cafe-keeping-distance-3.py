n=int(input())
arr=list(input())
for i in range(n):
    arr[i]=int(arr[i])

max_length=0
index=-1
cnt=0
for i in range(n):
    if arr[i]==0:
        cnt+=1
    elif arr[i]==1:
        if max_length<cnt:
            max_length=cnt
            index=i
        cnt=0
index=(index-max_length)+max_length//2
arr[index]=1
last_index=0
min_length=n
for i in range(1,n):
    if arr[i]==1:
        min_length=min(i-last_index,min_length)
        last_index=i
print(min_length)