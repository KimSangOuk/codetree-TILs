n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
answer=0
case_a_b=[]
case_c_d=[]
for i in range(n):
    for j in range(n):
        case_a_b.append(a[i]+b[j])
for i in range(n):
    for j in range(n):
        case_c_d.append(c[i]+d[j])
for i in range(len(case_a_b)):
    for j in range(len(case_c_d)):
        if case_a_b[i]+case_c_d[j]==0:
            answer+=1
print(answer)