n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

answer=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            first=str(arr[i]).zfill(4)
            second=str(arr[j]).zfill(4)
            third=str(arr[k]).zfill(4)

            carry=False
            for t in range(4):
                if int(first[t])+int(second[t])+int(third[t])>=10:
                    carry=True
                    break
            if not carry:
                answer=max(arr[i]+arr[j]+arr[k],answer)

if answer==0:
    print(-1)
else:
    print(answer)