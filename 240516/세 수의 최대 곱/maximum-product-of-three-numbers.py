n=int(input())
arr=list(map(int,input().split()))
yang=[]
eum=[]
zero=False
for i in range(n):
    if arr[i]>0:
        yang.append(arr[i])
    elif arr[i]<0:
        eum.append(arr[i])
    elif arr[i]==0:
        zero=True
yang.sort(reverse=True)
eum.sort()
possible=[]
if len(yang)>=3:
    possible.append(yang[0]*yang[1]*yang[2])
if len(yang)>=2 and len(eum)>=1:
    if zero:
        possible.append(0)
    else:
        possible.append(yang[-1]*yang[-2]*eum[-1])
if len(yang)>=1 and len(eum)>=2:
    possible.append(yang[0]*eum[0]*eum[1])
if len(eum)>=3:
    if zero:
        possible.append(0)
    else:
        possible.append(eum[-1]*eum[-2]*eum[-3]) 
print(max(possible))