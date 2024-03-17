n,m = map(int,input().split())

coins=[]
for i in range(n):
    coins.append(int(input()))

coins = sorted(coins)
print(coins)

d = [10001] * (m+1)

d[0] = 0

for coin in coins:
    for i in range(coin,m+1):
        if d[i-coin]!=10001:
            d[i] = min(d[i], d[i-coin] +1 )

print(d)


