#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    int answer_size = number.size()-k;
    int start_idx = 0;
    for(int i=0; i<answer_size; i++){
        char maxNum = number[start_idx];
        int maxIdx = start_idx;
        for (int j=start_idx; j<=k+i; j++){
            if (maxNum<number[j]){
                maxNum = number[j];
                maxIdx = j;
            }
        }
        answer += maxNum;
        start_idx = maxIdx+1;
    }
    
    
    return answer;
}