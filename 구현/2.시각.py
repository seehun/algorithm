def time(sec):
    #hour
    hour = sec//3600
    sec = sec - (hour*3600)

    #min
    minute = sec//60
    sec = sec- (minute*60)

    return [hour,minute,sec]


# print(time(5103))  
# 1 ,25 , 3


# 문자열에서 포함된 문자를 찾고 싶다면 "3" in "333"

n = int(input())
result =0

total_sec = n*3600 + 59*60 + 59

for num in range(0,total_sec+1):
    time_num_list = time(num)
    time_str = ""+str(time_num_list[0])+str(time_num_list[1])+str(time_num_list[2])
    # print(time_str)
    if("3" in time_str):
        result+=1

print(result)