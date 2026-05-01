#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
using namespace std;

int main(){
    string s;
    cin >> s;

    // create a std::string for the first half to avoid variable-length C arrays
    string cutf = s.substr(0, (s.length()+1)/2);
    string cutb = s.substr((s.length()+1)/2, s.length() - (s.length()+1)/2);
    
    printf(cutf.c_str(),cutb.c_str());

    return 0;
}