  #include <bits/stdc++.h>                                                                                
  using namespace std;                                                                                    
                                                                                                          
  int main() {                                                                                            
      long long W, B;                                                                                     
      if (!(cin >> W >> B)) return 0;                                                                     
      long long n = (1000 * W) / B + 1;                                                                   
      cout << n << '\n';                                                                                  
      return 0;                                                                                           
  }   