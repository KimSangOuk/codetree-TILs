alpha=dict()
s=list(input())
for i in s:
    if i in alpha:
        alpha[i]+=1
    else:
        alpha[i]=1
answer_list=[]
for i in alpha:
    if alpha[i]==1:
        answer_list.append(i)
find=False
for i in s:
    if i in answer_list:
        find=True
        print(i)
        break
if not find:
    print("None")