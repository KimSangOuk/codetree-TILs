n=int(input())
answer=0
dp=[int(1e9)]*50001
dp[2]=1
dp[5]=1
for i in range(3,n+1):
    dp[i]=min(dp[i-2],dp[i-5])+1
print(dp[n])