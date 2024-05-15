n=int(input())
arr=list(input())
for i in range(n):
    arr[i]=int(arr[i])
last_index=0
for i in range(n):
    if arr[i]==1:
        last_index=i
        break

max_index_1_1=0
max_length_1_1=0
for i in range(1,n):
    if arr[i]==1:
        if max_length_1_1<i-last_index-1:
            max_length_1_1=i-last_index-1
            max_index_1_1=i
        last_index=i
end_zero_length=0
start_zero_length=0
if arr[0]==0:
    for i in range(n):
        if arr[i]==0:
            start_zero_length+=1
        else:
            break
if arr[-1]==0:
    for i in range(n-1,-1,-1):
        if arr[i]==0:
            end_zero_length+=1
        else:
            break
find_index=-1
if end_zero_length-1>max_length_1_1//2 and end_zero_length-1>start_zero_length-1:
    find_index=n-1
elif end_zero_length-1<start_zero_length-1 and start_zero_length-1>max_length_1_1//2:
    find_index=0
else:
    find_index=max_index_1_1-(max_length_1_1+1)//2
arr[find_index]=1
answer=n
last_index=0
for i in range(n):
    if arr[i]==1:
        last_index=i
        break
for i in range(1,n):
    if arr[i]==1 and i!=last_index:
        answer=min(answer,i-last_index)
        last_index=i
print(answer)