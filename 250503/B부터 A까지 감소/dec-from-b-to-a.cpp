#include <iostream>
using namespace std;

int main() {
    int a,b;
    cin >> a>>b;
    for (int i=0;i<b-a+1;i++){
        cout << b - i<<" ";
    }
    return 0;
}