seat_dict=dict()
n,k=map(int,input().split())
changes=[]
seat=[]

for i in range(1,n+1):
    seat_dict[i]=set([i])
    seat.append(i)

for i in range(k):
    changes.append(tuple(map(int,input().split())))

for i in range(3):
    for j in range(k):
        c1,c2=changes[j]
        seat_dict[seat[c1-1]].add(c2)
        seat_dict[seat[c2-1]].add(c1)
        seat[c1-1],seat[c2-1]=seat[c2-1],seat[c1-1]

for i in range(1,n+1):
    print(len(list(seat_dict[i])))