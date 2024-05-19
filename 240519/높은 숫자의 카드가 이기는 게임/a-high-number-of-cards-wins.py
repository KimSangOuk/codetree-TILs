n=int(input())
b_card=[]
a_card=[]
for i in range(1,n+1):
    b_card.append(int(input()))
for i in range(1,2*n+1):
    if i not in b_card:
        a_card.append(i)
b_card.sort()
a_card.sort()
a_index=0
b_index=0
score=0
while a_index<n and b_index<n:
    if b_card[b_index]<a_card[a_index]:
        score+=1
        a_index+=1
        b_index+=1
    elif b_card[b_index]>a_card[a_index]:
        a_index+=1
print(score)