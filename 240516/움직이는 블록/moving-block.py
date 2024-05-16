n=int(input())
arr=[]
total=0
for i in range(n):
    arr.append(int(input()))
same=sum(arr)//len(arr)
double_answer=0
for i in range(n):
    double_answer+=abs(arr[i]-same)
print(double_answer//2)