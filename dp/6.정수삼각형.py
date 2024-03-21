# 376

n = 5

dp=[
    [7],
    [3,8],
    [8,1,0],
    [2,7,4,4],
    [4,5,2,6,5]
]

for i in range(1,n):  # 1~4
    for j in range(i+1):

        if j-1 <= -1:
            left_up = 0
        else: 
            left_up = dp[i-1][j-1]

        if j>=i:
            right_up=0
        else:
            right_up =dp[i-1][j]

        dp[i][j] +=max(left_up, right_up)

for i in range(n):
    print(dp[i], end='\n')

print(max(dp[n-1]))
