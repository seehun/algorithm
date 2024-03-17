arr= [2,4,1,3,8,5,7]

result = sorted(arr)  # 원본은 바뀌지 않음
print(arr)
print(result)

reverse = sorted(arr,reverse=True)
print(reverse)


arr2 = [('banana',2),('apple',5),('pineapple',3)]
result2 = sorted(arr2,key=lambda x : x[1])
print(result2)