#include <iostream>
using namespace std;

int main(){
    for (int i=0;i<10;i++){
        if (i==5){
            cout<<"skip"<<endl;
            continue;
        }
        else if (i==7){
            cout << "stop" << endl;
            break;
        }

        cout<<i<<endl;
    }
}