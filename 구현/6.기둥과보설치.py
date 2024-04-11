# 329

n=5
# build_frame =[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]


def solution(n, build_frame):
    # a , 0 기둥 1 보   
    # b , 0 삭제 1 설치 
    answer = []  
    # build_frame 에서 조건을 만족하면 answer에 값 넣기 
    for build in build_frame:
        x,y,a,b = build
        if a==0: # 기둥
            if b==0: #삭제
                # 다른 기둥 위에 있으면 X
                if [x,y+1,0] in answer:
                    continue
                # 기둥 위에 보가 없어야 함
                if [x,y+1,1] in answer and [x-1,y-1,1] in answer:
                    continue
                #삭제 ㄱ
                answer.remove([x,y,0])
                continue
            if b==1: #설치
                #바닥 위에 있는 경우 => 설치
                if y==0:  
                    answer.append([x,y,0])
                    continue
                #바닥 위에 없는 경우
                else: 
                    #다른 기둥 위에 있는 경우
                    if [x,y-1,0] in answer:
                        answer.append([x,y,0])
                        continue
                    # 보의 한쪽 끝부분 위에 있는 경우 (right or left)
                    if [x-1,y,1] in answer or [x,y,1] in answer:
                        answer.append([x,y,0])
                        continue
            continue
        if a==1: # 보
            if b==0: #삭제
                # 한쪽 끝부분이 기둥 위에 있는 경우  (오른쪽 or 왼쪽) -> X
                if [x,y-1,0] in answer or [x+1,y-1,0] in answer:
                    continue
                # 양쪽 끝부분이 다른 보와 동시에 연결 -> x
                if [x-1,y,1] in answer and [x+1,y,1] in answer:
                    continue
                answer.remove([x,y,1])
                continue
            if b==1: #설치
                # 한쪽 끝부분이 기둥 위에 있는 경우  (오른쪽 or 왼쪽)
                if [x,y-1,0] in answer or [x+1,y-1,0] in answer:
                    answer.append([x,y,1])
                    continue
                # 양쪽 끝부분이 다른 보와 동시에 연결
                if [x-1,y,1] in answer and [x+1,y,1] in answer:
                    answer.append([x,y,1])
                continue
            continue
        
    print(answer)
    # answer 정렬
    # x,y, a 순으로 정렬
    answer = sorted(answer, key= lambda x: (x[0],x[1],x[2]) )
    print(answer)
    
    return answer

solution(n,build_frame)