#include <iostream>
#include <cstring>
using namespace std;

int T, N, nList[1001], dp[1001][1001];

int cardGame(int left, int right, int turn);

int main() {
  cin >> T;

  while (T--) {
    cin >> N;
    for (int i=1; i<=N; i++) {cin >> nList[i];}

    cardGame(1, N, 1);
    cout << dp[1][N] << '\n';
    memset(dp, 0, sizeof(dp));
  }

  return 0;
}

int cardGame(int left, int right, int turn) {
  if (left > right) {return 0;}
  if (dp[left][right]) {return dp[left][right];}

  if (turn % 2 == 1) { // 근우 턴
    dp[left][right] = max(nList[left] + cardGame(left+1, right, turn+1), nList[right] + cardGame(left, right-1, turn+1));
    return dp[left][right];
  }
  else { // 명우 턴
    dp[left][right] = min(cardGame(left+1, right, turn+1), cardGame(left, right-1, turn+1));
    return dp[left][right];
  }
}