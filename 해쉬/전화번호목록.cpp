#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

//내 풀이 -> 시간초과

bool solution(vector<string> phone_book) {
    bool answer = true;
    
    for (int i=0; i<phone_book.size(); i++){
        string front = phone_book[i];
        int front_size = phone_book[i].size();
        
        for (int j=0; j<phone_book.size(); j++){
            if(i==j){
                continue;
            }else{
                string num = phone_book[j];
                if (front == num.substr(0,front_size)){    //  문자열 슬라이싱
                    return false;
                }
            }
        }
        
    }
    
    return answer;
}

//정렬 풀이법

bool solution(vector<string> phone_book) {
    bool answer = true;
   
    sort(phone_book.begin(),phone_book.end());
    
    for (int i=0;i<phone_book.size()-1;i++){
        if(phone_book[i] == phone_book[i+1].substr(0,phone_book[i].size()))
            return false;
    }
    
    
    return answer;
}