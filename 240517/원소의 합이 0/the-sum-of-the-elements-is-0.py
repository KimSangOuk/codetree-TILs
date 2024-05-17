n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
case_a_b=dict()
case_c_d=dict()
for i in range(n):
    for j in range(n):
        if a[i]+b[j] in case_a_b:
            case_a_b[a[i]+b[j]]+=1
        else:
            case_a_b[a[i]+b[j]]=1
for i in range(n):
    for j in range(n):
        if c[i]+d[j] in case_c_d:
            case_c_d[c[i]+d[j]]+=1
        else:
            case_c_d[c[i]+d[j]]=1
answer=0
for i in list(set(case_a_b.keys())):
    for j in list(set(case_c_d.keys())):
        if i==j and i==0:
            answer+=(case_a_b[i])*(case_c_d[j])
        else:
            if i+j==0:
                answer+=(case_a_b[i])*(case_c_d[j])
print(answer)