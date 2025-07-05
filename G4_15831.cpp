#include <iostream>
using namespace std;

int main() {
  int n, b, w;
  int B{0}, W{0};
  cin >> n >> b >> w;

  char *cList = new char[n];
  for (int i=0; i < n; i++) {cin >> cList[i];}

  int s{0}, e{0}, maxLen{0};
  while (e < n) {
    if (cList[e] == 'W') {W++;}
    else {B++;}

    while (B > b) {
      if (cList[s] == 'W') {W--;}
      else {B--;}
      s++;
    }

    if (W >= w) {maxLen = max(maxLen, e-s+1);}

    e++;
  }

  cout << maxLen;

  return 0;
}