#p.115

input_data = input()

row = int(input_data[1])
column = ord(input_data[0]) - ord('a') +1

print(row,column)

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0
for step in steps:
    next_row = column+step[1]
    next_column = row + step[0]

    if(next_row<1 or next_row>8 or next_column<1 or next_column>8):
        continue
    else:
        result+=1

print(result)