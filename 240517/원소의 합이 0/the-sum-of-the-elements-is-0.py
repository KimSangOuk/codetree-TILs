from itertools import product

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
answer=0
for arr in product(a,b,c,d):
    if sum(arr)==0:
        answer+=1
print(answer)