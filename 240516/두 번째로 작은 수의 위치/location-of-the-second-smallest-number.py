import copy

n=int(input())
arr=list(map(int,input().split()))
find_arr=copy.deepcopy(arr)
arr=sorted(list(set(arr)))
if len(arr)<2:
    print(-1)
else:
    for i in range(1,n+1):
        if find_arr[i-1]==arr[1]:
            print(i)
            break