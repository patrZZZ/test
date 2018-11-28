

#include <iostream>
using namespace std;


int main() {
   cout << "Hello World"; // prints Hello World
   return 0;
}

sizeof()

int sockMerchant(int n, vector<int> ar) {
    vector<int>::iterator it = ar.begin();
    int pairs = 0;
    for(;it<ar.end();it++){
        int start = *it;
        vector<int>::iterator it2 = it + 1;
        for(;it2<ar.end();){
            if(*it2 == start){
                pairs = pairs + 1;
                ar.erase(it2); 
                break;
            }
            else{
                it2++;
            ｝
        }
    }
    return pairs;
}

int countingValleys(int n, string s) {
    int level = 0;
    int valley = 0;
    vector<int> levels;
    levels.push_back(level);
    for(int i = 0; i<n; i++){
        if(s[i]=='U'){
            level+=1;
        }
        else{
            level-=1;
        }
        levels.push_back(level);
    }
    for(int i = 1; i < levels.size(); i++){
        if(levels[i]<0&&levels[i-1]==0){
            valley+=1;
        } 
    }
    return valley;
}
   
int jumpingOnClouds(vector<int> c) {
    int length = c.size();
    int steps = 0;
    for(int i = 0; i <length;){
        steps+=1;
        if(i+2<length && c[i+2]==0){
            i = i+2;
        }
        else{
            i = i+1;
        }
        cout<<i<<endl;
    }
    return steps-1;
}  
   
long repeatedString(string s, long n) {
    long a_num = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i]=='a'){
            a_num += 1;
        }
    }
    long repet_num = n/s.size();
    long remain = n%s.size();
    long re_num = 0;
    for (int i = 0; i <remain; i++){
        if(s[i] =='a'){
            re_num += 1;
        }
    }
    long num = a_num * repet_num + re_num;
    return num;
}

   

      
