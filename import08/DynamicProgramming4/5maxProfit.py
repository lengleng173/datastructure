def maxProfit(prices):
    n=len(prices)
    dp=[[0 for _ in range(2)] for _ in range(n+1)]
    dp[1][0]=0
    dp[1][1]=-prices[0]
    for idx in range(2,len(prices)+1):
        dp[idx][0]=max(dp[idx-1][0],dp[idx-1][1]+prices[idx-1])
        dp[idx][1]=max(-prices[idx-1],dp[idx-1][1])
    return dp[n][0]
print(maxProfit([7,1,5,3,6,4]))