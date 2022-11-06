def climbStairs(n):
    if n == 1:
        return 1

    dp = {}
    dp[1] = 1
    dp[2] = 2

    i = 3

    while i <= n:
        dp[i] = dp[i-1] + dp[i-2]
        i += 1
        
    return dp[n]
