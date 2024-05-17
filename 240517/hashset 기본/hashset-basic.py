arr=set()
n=int(input())
for i in range(n):
    s,t=map(str,input().split())
    if s=='find':
        if int(t) in arr:
            print('true')
        else:
            print('false')
    elif s=='add':
        arr.add(int(t))
    elif s=='remove':
        arr.remove(int(t))