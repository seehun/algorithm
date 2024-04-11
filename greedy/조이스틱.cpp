#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(string name) {
    int answer = 0;
    string initial_name;
    
    for(int i=0; i<name.length(); i++){
        initial_name+='A';
    }
    int current =0;
    
    while(true){
        
        //헌재 알파벳이 다를 때
        if (initial_name[current]!=name[current]){
            // 위 아래 이동
            answer+=min(name[current]-'A','Z'-name[current]+1);
            initial_name[current]= name[current];
        }
        if (initial_name==name){
            return answer;
        }
        
        // 이동
        
        //1. 왼쪽 이동횟수 구하기
        int left_index = current;
        int left_cnt=0;
        while (initial_name[left_index]==name[left_index]){
            if(left_index==0){ // 맨처음일 경우 마지막으로 이동
                left_index = initial_name.length()-1;
                left_cnt++;
                continue;
            }
            left_index-=1;
            left_cnt++;
        }
        
        //2. 오른쪽 이동횟수 구하기
        int right_index = current;
        int right_cnt=0;
        while (initial_name[right_index]==name[right_index]){
            if(right_index==initial_name.length()-1){ // 맨마지막일 경우 처음으로 이동
                right_index =0;
                right_cnt++;
                continue;
            }
            right_index+=1;
            right_cnt++;
        }
        
        // 둘 중 작은 이동횟수로 이동
        if(left_cnt<=right_cnt){
            current = left_index;
            answer+=left_cnt;            
        }else{
            current = right_index;
            answer+=right_cnt; 
        }
        
    }
}