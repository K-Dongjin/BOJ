#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  int a, m;
  a = n / 2;
  m = a + 1;
  for (int i=1; i <= n; i++) {
    if (i % 2 == 1) {cout << m++ << ' ';}
    else {cout << a-- << ' ';}
  }

  return 0;
}