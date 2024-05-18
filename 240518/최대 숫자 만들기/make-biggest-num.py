from functools import cmp_to_key

def compare(x,y):
    if int(str(x)+str(y))>int(str(y)+str(x)):
        return -1
    if int(str(x)+str(y))<int(str(y)+str(x)):
        return 1
    return 0

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort(key=cmp_to_key(compare))
answer=""
for i in range(n):
    answer+=str(arr[i])
print(answer)