#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vint;
typedef pair<int, int> pint;
typedef vector<pint> vpint;
#define rep(i,n) for(int i=0;i<(n);i++)
#define REP(i,n) for(int i=n-1;i>=(0);i--)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define each(it,v) for(__typedef((v).begin()) it=(v).begin;it!=(v).end();it++)
#define all(v) (v).begin().(v).end()
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define chmax(a, b) a = (((a)<(b)) ? (b) : (a))
#define chmin(a, b) a = (((a)>(b)) ? (b) : (a))
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll INFF = 1e18;

string N;
ll dp[12][2][12];
// dp[i][j][k] := i桁目まで見て，j==1ならNより小さい，1を使った数がk回となる 数字の総数


int main(void){
    cin >> N;
    rep(i, 12)rep(j, 2)rep(k, 12) dp[i][j][k] = 0;
    dp[0][0][0] = 1;

    rep(i, N.size()){
        rep(j, 2)rep(k, 12){
            if(dp[i][j][k] == 0) continue;
            if(j == 1){ // Nより小さい
                dp[i + 1][1][k+1] += dp[i][j][k]; // 1を選ぶ
                dp[i + 1][1][k] += dp[i][j][k] * 9; // 0,2,...,9を選ぶ
            }else{
                if(N[i] == '1'){
                    dp[i + 1][0][k + 1] += dp[i][j][k]; //1を選ぶ
                    dp[i + 1][1][k] += dp[i][j][k]; //0を選ぶ
                }else if(N[i] == '0'){
                    dp[i + 1][0][k] += dp[i][j][k]; //0を選ぶ
                }else{//2 <= N[i] <= 9
                    dp[i + 1][0][k] = dp[i][j][k]; // N[i]を選ぶ
                    dp[i + 1][1][k] = dp[i][j][k] * ((N[i] - '0') - 1); //2 ~ N[i]-1
                    dp[i + 1][1][k + 1] += dp[i][j][k]; //1を選ぶ
                }
            }
        }
    }
    ll ans = 0;
    rep(j, 2)rep(k, 12){
        if(dp[(int)N.size()][j][k]){
            ans += k * dp[(int)N.size()][j][k];
        }
    }
    cout << ans << endl;
    return 0;

}

