#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
using namespace std;

int main(){
    string s;
    cin >> s;

    // create a std::string for the first half to avoid variable-length C arrays
    string cut = s.substr(0, (s.length()+1)/2);
    printf("cut_top:%s\n", cut.c_str());

    return 0;
}