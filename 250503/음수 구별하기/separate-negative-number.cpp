#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n<0){
        cout <<n<<endl;
        cout <<"minus";
    }
    else if(n>=0){
        cout << n ;
    }
    return 0;
}