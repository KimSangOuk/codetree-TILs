n=int(input())
arr=dict()
for i in range(n):
    tmp=sorted(list(input()))
    if "".join(tmp) in arr:
        arr["".join(tmp)]+=1
    else:
        arr["".join(tmp)]=1
cnt=list()
for i in arr.keys():
    cnt.append((i,arr[i]))
cnt.sort(key=lambda x:-x[1])
print(arr[cnt[0][0]])