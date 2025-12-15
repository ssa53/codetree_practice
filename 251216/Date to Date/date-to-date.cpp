#include <iostream>
using namespace std;

int main() {
    int num_of_days[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
    int month1,day1,month2,day2;
    cin >> month1 >> day1 >> month2 >> day2;
    int rst=1;
    while(true){
        if(month1==month2&&day1==day2){
            break;
        }
        if(num_of_days[month1]==day1){
            month1 ++;
            day1=0;
        }
        day1 ++;
        rst++;
    }
    cout << rst;
    return 0;
}