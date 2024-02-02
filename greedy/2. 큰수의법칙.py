# n,m,k = map(int,input().split())
n,m,k = 5,8,3

# data = list(map(int,input().split()))
data =[2,4,5,4,6]

result = 0
data.sort(reverse=True)

#init

first = data[0]
second = data[1]

repeat= 0
for i in range(m):
    if(repeat==k):
        result +=second
        repeat=0
    else:
        result +=first
        repeat+=1
        



print(result)
    

    
