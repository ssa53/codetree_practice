#include <iostream>
using namespace std;

int main() {
    int temp;
    cin >> temp;
    if(temp>=100){
        cout <<"vapor";
    }
    else if(temp<100 && temp>=0){
        cout <<"water";
    }
    else{
        cout <<"ice";
    }
    return 0;
}