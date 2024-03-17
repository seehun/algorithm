# p.226


n,m  = map(int,input().split())

d= [10001]* 101

d[0]=0

coins=[]
for i in range(n):
    coins.append(int(input()))

coins = sorted(coins)


for coin in coins:
    d[coin] = 1

print(d)


for coin in coins:   # 2 3 5
    for i in range(coin,m+1):
        d[i] = min(d[i-coin]+1, d[i])

print(d)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

