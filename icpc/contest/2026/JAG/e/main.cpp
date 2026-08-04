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
#define REP_2(i, n) for (int i = 0; i < (int)(n); i++)
#define REP_3(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define REP_SELECT(_1, _2, _3, NAME, ...) NAME
#define sort2 [](const pl& a, const pl& b){return a.second < b.second;}
#define endl '\n'
constexpr ll INF=4*1e18;
const double pi = acos(-1.0);
const ll mod = 998244353;
const ll Mod = 1000000007;
template <typename T, typename U> inline bool chmin(T &x, U y) { return (y < x) ? (x = y, true) : false; }
template <typename T, typename U> inline bool chmax(T &x, U y) { return (x < y) ? (x = y, true) : false; }

int main() {
    int c=1;
    vl bita(34);
    vl bitb(34);
    vl mul(35);

        cout<<"?"<<" "<<0<<" "<<0;
        int e;cin>>e;
        c*=e;
        mul[31]=e;
        rep(i,0,31){
            cout<<"?"<<" "<<0<<" "<<1*c;
            int a;cin>>a;
            bita[i]=0;
            bitb[i]=1;
            mul[i]=a;
            if(a==1){
                cout<<"?"<<" "<<1*c<<" "<<0;
                int b;cin>>b;
                if(b==1){
                    cout<<"?"<<" "<<1*c<<" "<<1*c;
                    int d;cin>>d;
                    c*=d;
                    bita[i]=1;
                    bitb[i]=1;
                    mul[i]=d;
                }
                else{
                    c*=b;
                    bita[i]=1;
                    bitb[i]=0;
                    mul[i]=b;
                }
            }
            else{c*=a;break;}
        }
        int answera=1;
        int answerb=1;
        rep(i,0,31){
            answera=answera*mul[30-i]-bita[30-i];
            answerb=answerb*mul[30-i]-bitb[30-i];
        }
        answera*=mul[31];
        answerb*=mul[31];
        cout<<"!"<<" "<<answera<<" "<<answerb;
        return 0;
}