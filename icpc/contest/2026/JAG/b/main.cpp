#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;
using i128 = __int128;
using pl = pair<ll,ll>;
using vl = vector<ll>;
using vvl = vector<vector<ll>>;
#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define rep(i,a,b) for (int i=(int)(a);i<(int)(b);i++)
#define sort2 [](const pl& a, const pl& b){return a.second < b.second;}
#define endl '\n'
constexpr ll INF=4*1e18;
const double pi = acos(-1.0);
const ll mod = 998244353;
const ll Mod = 1000000007;
template <typename T, typename U> inline bool chmin(T &x, U y) { return (y < x) ? (x = y, true) : false; }
template <typename T, typename U> inline bool chmax(T &x, U y) { return (x < y) ? (x = y, true) : false; }

int main() {
    rep(i,0,100){
        ll N;cin>>N;
        if(N==0){break;}
        else{
            string s;cin>>s;
            int a=s.size();
            int count=0;
            int dif=0;
            rep(i,1,a){
                if(s[i]==s[0]){count++;}
                else if(dif==0){
                    dif=i;
                }
            }
            if(count==a-1){cout<<"IMPOSSIBLE"<<endl;}
            else{
                char c=s[0];
                s[0]=s[dif];
                s[dif]=c;
                cout<<s<<endl;
            }
        }
    }
    return 0;
}
