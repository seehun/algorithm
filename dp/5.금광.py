# 375

n,m = 3,4


dp = [
    [1,3,3,2],
    [2,1,4,1],
    [0,6,4,7]
]


for i in range(1,m):
    for j in range(n):  # dp[j][i]

        if j-1 >=0:
            left_up = dp[j-1][i-1]
        else:
            left_up =0
        
        left = dp[j][i-1]

        if j+1<=n-1:
            left_down = dp[j+1][i-1]
        else:
            left_down = 0 

        dp[j][i]+= max(left_up,left,left_down)

print(dp)

result =0 
for i in range(n):
    result = max(dp[i][m-1],result)
print(result)
        
        
        
