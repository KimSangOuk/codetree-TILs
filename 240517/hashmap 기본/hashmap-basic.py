n=int(input())
arr=dict()
for i in range(n):
    c=list(map(str,input().split()))
    if c[0]=="add":
        arr[c[1]]=c[2]
    elif c[0]=="find":
        if c[1] in arr:
            print(arr[c[1]])
        else:
            print("None")
    elif c[0]=="remove":
        arr.pop(c[1])