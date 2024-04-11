#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.rbegin(),people.rend());
    
    int currentLimit=0;
    int start=0;
    int end = people.size()-1; 
    while(start<=end){
        if (people[start]+people[end]<=limit){
            answer+=1;
            start+=1;
            end-=1;
        }else{
            answer+=1;
            start+=1;
        }
    }
    return answer;
}