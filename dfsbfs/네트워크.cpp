#include <string>
#include <vector>
#define MAX 200

using namespace std;

int answer = 0;
bool connected[MAX] ={0};

int dfs(int current , vector<vector<int>> computers){
    connected[current] = true;
    for(int i=0; i<computers[current].size(); i++){
        if(current == i){
            continue;
        }else{
            if(computers[current][i]==1 && connected[i]==false){
                connected[i]=true;
                dfs(i,computers);    
            }
        }
    }
    return 1;
}

int solution(int n, vector<vector<int>> computers) {
    for (int i=0;i<n;i++){
        if(connected[i]==false){
            answer+=dfs(i,computers);
        }
    }
    
    
    return answer;
}