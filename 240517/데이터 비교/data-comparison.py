import sys
n=int(input())
arr1=list(map(int,sys.stdin.readline().split()))
m=int(input())
arr2=list(map(int,sys.stdin.readline().split()))

for i in arr2:
    if i in set(arr1):
        print(1,end=' ')
    else:
        print(0,end=' ')