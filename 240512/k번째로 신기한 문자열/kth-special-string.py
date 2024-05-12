n,k,T=map(str,input().split())
n,k=int(n),int(k)

arr=list()
for i in range(n): 
    s=input()
    if T==s[0:len(T)]:
        arr.append(s)

arr.sort()
print(arr[k-1])