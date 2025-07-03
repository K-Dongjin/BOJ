#include <iostream>
using namespace std;

const int MOD = 1000000007;

int palCnt(int n, int m);
int main() {
  int n, m, k;
  cin >> n >> m >> k;

  if ((k == 1) || (k > n)) {
    long long ans = 1;
    while (n--) {ans = (ans * m) % MOD;}
    cout << ans << '\n';
  }
  else if (n == k) {cout << palCnt(n, m) << '\n';}
  else if (n > k) {
    if (k % 2 == 0) {cout << m << '\n';}
    else {cout << m * m << '\n';}
  }

  return 0;
}

int palCnt(int n, int m) {
  long long temp, ret{1};
  if (n % 2 == 0) {temp = n / 2;}
  else {temp = (n / 2) + 1;}
  while (temp--) {ret = (ret * m) % MOD;}
  return ret;
}