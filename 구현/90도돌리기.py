def rotate_90_degree(a):
    n = len(a)
    m= len(a[0])
    result = [[0]*n for i in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result




arr = [
    [1,0,0],
    [0,1,1],
    [1,0,1]
]

arr2 = rotate_90_degree(arr)
print(arr2)
