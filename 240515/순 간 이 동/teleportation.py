a,b,x,y=map(int,input().split())
answer=min(abs(a-x)+abs(y-b),abs(a-y)+abs(b-x))
print(min(answer,abs(a-b)))