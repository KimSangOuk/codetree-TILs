n,m=map(int,input().split())
jewels=[]
for i in range(n):
    w,v=map(int,input().split())
    jewels.append((v/w,w,v))
jewels.sort(reverse=True)
now=0
answer=0
for v_w,w,v in jewels:
    if now+w>m:
        answer+=v*(m-now)/w
        break
    else:
        answer+=v
        now+=w
        if now==m:
            break
print("{:.3f}".format(round(answer,3)))