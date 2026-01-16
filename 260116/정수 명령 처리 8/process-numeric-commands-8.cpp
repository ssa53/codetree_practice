#include <iostream>
#include <list>
using namespace std;

int main() {
    // Please write your code here.
    list<int> l;
    int n;cin>>n;
    for(int i=0;i<n;i++){
        string cmd;
        cin>>cmd;
        if(cmd=="push_back"){
            int inp;
            cin>>inp;
            l.push_back(inp);
        }
        else if(cmd=="push_front"){
            int inp;cin>>inp;
            l.push_front(inp);
        }
        else if(cmd=="pop_front"){
            cout << l.front() << endl;
            l.pop_front();
        }
        else if(cmd=="pop_back"){
            cout<<l.back()<<endl;
            l.pop_back();
        }
        else if(cmd=="size"){
            cout << l.size()<<endl;
        }
        else if(cmd=="empty"){
            cout << l.empty()<<endl;
        }
        else if(cmd=="front"){
            cout << l.front()<<endl;
        }
        else if(cmd=="back"){
            cout << l.back()<<endl;
        }
    }
    return 0;
}