n,k=map(int,input().split())

length=0
alpha_man=[]
for i in range(n):
    pos,alpha=input().split()
    alpha_man.append((int(pos),alpha))
    length=max(length,int(pos))

arr=[0]*length
for pos,alpha in alpha_man:
    if alpha=='G':
        arr[pos-1]=1
    elif alpha=='H':
        arr[pos-1]=2

answer=0
for i in range(length-k+2):
    answer=max(answer,sum(arr[i:i+k+1]))

print(answer)