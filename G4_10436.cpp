#include <cstdio>
#include <deque>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);

  while (T--) {
    int t, p, q, nxtP, nxtQ, cnt{0};
    scanf("%d %d/%d", &t, &p, &q);

    if (q == 1) {nxtP = 1; nxtQ = p+1;}
    else {
      cnt = p/q; p %= q;
      nxtP = q; nxtQ = (q-p) + (q*cnt);
    }

    printf("%d %d/%d\n", t, nxtP, nxtQ);
  }

  return 0;
}