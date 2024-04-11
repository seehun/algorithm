#346

n=6
numbers =[1,2,3,4,5,6]

add,sub,mul,div =[2,1,1,1]   #  +  -  *  //

max_value = -1e9
min_value =1e9



def dfs(i,now):
    global max_value,min_value,add,sub,mul,div

    if i==n:
        max_value = max(max_value,now)
        min_value = min(min_value,now)
        return
    
    else:
        if add>0:
            add= add-1
            dfs(i+1,now+numbers[i])
            add+=1
        if sub>0:
            sub= sub-1
            dfs(i+1,now-numbers[i])
            sub+=1
            
        
        if mul>0:
            mul= mul-1
            dfs(i+1,now*numbers[i])
            mul+=1
            
        
        if div>0:
            div= div-1
            dfs(i+1,int(now/numbers[i]))
            div+=1
            

dfs(1,numbers[0])  
print(max_value,min_value)




