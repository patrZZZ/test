

#include <iostream>
#include <string>
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

 while(condition) {
   statement(s);
}

if(boolean_expression 1) {
   // Executes when the boolean expression 1 is true
} else if( boolean_expression 2) {
   // Executes when the boolean expression 2 is true
} else if( boolean_expression 3) {
   // Executes when the boolean expression 3 is true
} else {
   // executes when the none of the above condition is true.
}

   
   char grade = 'D';

   switch(grade) {
      case 'A' :
         cout << "Excellent!" << endl; 
         break;
      case 'B' :
      case 'C' :
         cout << "Well done" << endl;
         break;
      case 'D' :
         cout << "You passed" << endl;
         break;
      case 'F' :
         cout << "Better try again" << endl;
         break;
      default :
         cout << "Invalid grade" << endl;
   }
   cout << "Your grade is " << grade << endl;

//Array:
int a[3][4] = {  
   {0, 1, 2, 3} ,   
   {4, 5, 6, 7} ,   
   {8, 9, 10, 11}   
};
int a[3][4] = {0,1,2,3,4,5,6,7,8,9,10,11};
   
double *p;
double balance[10];

p = balance;
   
*(p+1)
   
char greeting[] = "Hello";
  

string str1 = "Hello";
string str2 = "World";

str3 = str1 + str2;
len = str3.size();

   
struct Books {
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} 
void printBook( struct Books book )
   
struct Books *struct_pointer;
struct_pointer = &Book1;
struct_pointer->title;
   
class Box {
   public:
      double length;   // Length of a box
      double breadth;  // Breadth of a box
      double height;   // Height of a box
};
   
double Box::getVolume(void) {
   return length * breadth * height;
}
   
Box::Box(double length) {
   cout << "Object is being created" << endl;
}
Box::~Box(void) {
   cout << "Object is being deleted" << endl;
}
//copy constructor
Line::Line(const Line &obj) {
   cout << "Copy constructor allocating ptr." << endl;
   ptr = new int;
   *ptr = *obj.ptr; // copy the value
}
//Derived class
class Rectangle: public Shape {
   public:
   a = 1；
      ｝
class Rectangle: public Shape, public PaintCost { 



   
   
