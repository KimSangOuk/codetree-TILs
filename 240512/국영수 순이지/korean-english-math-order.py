n=int(input())
arr=list()
for i in range(n):
    name,kuk,eng,math=map(str,input().split())
    arr.append((name,int(kuk),int(eng),int(math)))
arr.sort(key=lambda x:(-x[1],-x[2],-x[3]))
for i in range(n):
    print(*arr[i])