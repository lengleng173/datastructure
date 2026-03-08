def numWay(n):
    if n==0 or n==1:return 1
    if n==2:return 2
    dp=[[0 for _ in range(2)]for _ in range(n+1)]
    dp[1][0]=1
    dp[2][0]=1
    dp[2][1]=1
    for i in range(3,n+1):
        dp[i][0]=dp[i-1][0]+dp[i-1][1]
        dp[i][1]=dp[i-2][0]+dp[i-2][1]
    return dp[n][0]+dp[n][1]



print(numWay(7))