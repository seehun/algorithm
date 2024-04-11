#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string target="";
string aeiou = "AEIOU";
int answer =0;
int cnt =-1;

void dfs(string word){
    cnt++;
    if(word == target){
        answer = cnt;
        return;
    }
    
    if (word.size()>=5) return;
    
    for (int i=0;i<5;i++){
        dfs(word+aeiou[i]);
    }
}

int solution(string word) {
    target= word;   //target-> AAAAE
    dfs("");
    return answer;
}