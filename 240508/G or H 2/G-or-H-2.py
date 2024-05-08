n=int(input())
arr=[]

for i in range(n):
    pos,alpha=input().split()
    arr.append((int(pos),alpha))

arr.sort()
answer=0
for i in range(len(arr)):
    g_cnt,h_cnt=0,0
    if arr[i][1]=='G':
        g_cnt+=1
    else:
        h_cnt+=1
    # print("시작 지점",arr[i][0],arr[i][1])
    for j in range(i+1,len(arr)):
        if arr[j][1]=='G':
            g_cnt+=1
        else:
            h_cnt+=1
        if g_cnt==h_cnt or h_cnt==0 or g_cnt==0:
            # print("업데이트",arr[j][0],arr[j][1])
            answer=max(arr[j][0]-arr[i][0],answer)
print(answer)