n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

answer=int(1e9)
for i in range(n):
    start=i
    sum_value=0
    for j in range(n):
        dist=0
        if j<start:
            dist=n-(start-j)
        else:
            dist=j-start
        sum_value+=dist*arr[j]
    answer=min(sum_value,answer)
print(answer)