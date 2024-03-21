n,m = 3,4


dp = [
    [1,3,3,2],
    [2,1,4,1],
    [0,6,4,7]
]

dx= []
dy= []

for i in range(n):
    for j in range(1,m):
        if i-1 == -1:
            left_up =0
            dp[i][j] += max( left_up, dp[i][j-1], dp[i+1][j-1] )
            continue
        if i+1>=n:
            left_down =0
            dp[i][j] += max( dp[i-1][j-1], dp[i][j-1], left_down)
            continue
        
        dp[i][j] += max( dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1] )

print(dp)
        

