

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
            }

        }
    }
    return pairs;

}
