#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#define MAX 8

using namespace std;

int answer=-1;
bool visited[MAX] = {0};

void dfs(int cnt, int k,vector<vector<int>> dungeons){
    answer = max(cnt,answer);
    for (int i=0; i<dungeons.size(); i++){
        if(visited[i]==false && dungeons[i][0]<=k){
            visited[i]=true;
            dfs(cnt+1,k-dungeons[i][1],dungeons);
            visited[i]=false;
        }
    }
}
int solution(int k, vector<vector<int>> dungeons) {
    dfs(0,k,dungeons);  //  현재 탐헌한 던전, 현재 피로도, 던전 데이터
    return answer;
}