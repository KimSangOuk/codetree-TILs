n=int(input())
arr=list()
for i in range(n):
    name,score1,score2,score3=map(str,input().split())
    score1,score2,score3=int(score1),int(score2),int(score3)
    arr.append((name,score1,score2,score3))
arr.sort(key=lambda x:x[1]+x[2]+x[3])
for i in range(n):
    print(*arr[i])