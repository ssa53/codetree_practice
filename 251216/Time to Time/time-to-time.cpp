#include <iostream>
using namespace std;

int main() {
    int a,b,c,d;
    cin >> a >> b >> c >> d;
    int min=0;
    while (true){
        if(a==c && b==d){
            break;
        }
        if(b==59){
            a ++;
            b=0;
        }
        else{
            b++;
        }
        min ++;
    }
    cout << min;
    return 0;
}