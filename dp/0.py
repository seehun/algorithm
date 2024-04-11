n=7
t=[3,5,1,1,2,4,2]
p=[10,20,10,20,15,40,200]
max_value=0

dp=[0] * n

for i in range(n-1,-1,-1):
    if i + t[i] <= n:
        dp[i] = p[i]
        for j in range(i,n):
            dp[i] = max(p[i]+dp[i+t[i]], dp[i])

print(max(dp))

