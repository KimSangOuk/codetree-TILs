a,b,c=map(int,input().split())
arr=[a,b,c]
arr.sort()
if arr[1]-arr[0]==1 and arr[2]-arr[1]==1:
    print(0)
elif arr[1]-arr[0]==2 or arr[2]-arr[1]==2:
    print(1)
else:
    print(2)