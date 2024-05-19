n=int(input())
b_card=[]
a_card=[]
for i in range(n):
    b_card.append(int(input()))
for i in range(1,2*n+1):
    if i not in b_card:
        a_card.append(i)
b_card.sort()
a_card.sort()
a_index=0
b_index=0
score=0
for i in range(len(b_card)):
    if b_card[i]<a_card[a_index]:
        score+=1
        a_index+=1
        if a_index>=len(a_card):
            break
    else:
        a_index+=1
        if b_card[i]<a_card[a_index]:
            score+=1
            a_index+=1
            if a_index>=len(a_card):
                break
print(score)