// Recursive Fibonacci sequence -> C++
#include <iostream>
using namespace std;
#include <string>
#include <algorithm>




// Function input should be an Integer
int fibFunc(int x){
  if(x==0 || x==1){
    return x;
  }
  return fibFunc(x-1)+fibFunc(x-2);
}


int main() {
  //cout<<fibFunc(8)<<endl;
}