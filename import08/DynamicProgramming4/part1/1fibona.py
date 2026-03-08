def fabona(n):
    if n==0:return 0
    if n==1:return 1
    dp=[0 for _ in range(n+1)]
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]%100000000007
print(fabona(100))