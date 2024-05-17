n,m=map(int,input().split())
digit_to_alpha=dict()
alpha_to_digit=dict()
for i in range(1,n+1):
    s=input()
    digit_to_alpha[i]=s
    alpha_to_digit[s]=i

for i in range(m):
    s=input()
    if s.isdigit():
        print(digit_to_alpha[int(s)])
    else:
        print(alpha_to_digit[s])