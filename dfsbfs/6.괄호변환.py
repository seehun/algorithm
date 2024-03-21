#346



result = ''

def separate(sentence):
    count_right =0
    count_left=0
    u=''
    v=''
    for i in range(len(sentence)):
        if sentence[i]=='(':
            count_right+=1
        else:
            count_left+=1    

        if count_right!=0 and count_left!=0 and count_right==count_left:
            u = sentence[:i+1]
            v= sentence[i+1:]
            break
    return u,v


# u,v = separate(p)
# print(u)
# print(v)

def correct(words):
    if words[0]== '(':
        return True
    else:
        return False
    
def change_u(words):
    if len(words)==0:
        return ''

    result =''
    for word in words:
        if word=='(':
            result+=')'
        else:
            result+='('
    return result[1:len(result)-1]




def dfs(sentence):
    global result

    if sentence== '':  # 빈문자열이라면
        return ''

    u,v = separate(sentence)
    if correct(u): # u가 올바른 문자열이라면
        result+=u+dfs(v)
        return result
        
        
    else: # 올바른 문자열이 아니라면
        result += '('+ dfs(v) + ')' + change_u(u)
        return result
        
p='(()())()'
# p = '()))((()'
# p=')('
dfs(p)
print(result)






