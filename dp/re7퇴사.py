# 377


# n=7

# t=[0,3, 5,  1, 1, 2, 4, 2]
# p=[0,10,20,10,20,15,40,200]
n=7
t=[3,5,1,1,2,4,2]
p=[10,20,10,20,15,40,200]
max_value=0

dp =[0]* (n+1) 
print(dp)

for i in range(n,0,-1):
    print(i)
    
    if i+t[i]<=n: #기간 안에 상담을 받을 수 있는 경우
        dp[i] = max(p[i]+dp[i+t[i]],max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

    

print(dp)
print(max_value)

