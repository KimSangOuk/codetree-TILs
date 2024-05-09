n,b=map(int,input().split())
price_list=list()
for i in range(n):
    price=int(input())
    price_list.append(price)
price_list.sort()

answer=0

for i in range(n):
    total=0
    num=0
    for j in range(n):
        if i==j:
            total+=price_list[j]//2
        else:
            total+=price_list[j]
        if total<=b:
            num+=1
    answer=max(num,answer)
print(answer)