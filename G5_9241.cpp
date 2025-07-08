#include <iostream>
using namespace std;

int main() {
  string a, b;
  cin >> a >> b;
  int al{a.length()}, bl{b.length()}, s{0};
  
  while ((s < min(al, bl)) && (a[s] == b[s])) {s++;}

  al--; bl--;
  while ((al >= s) && (bl >= s) && (a[al] == b[bl])) {al--; bl--;}

  if (s >= min(a.length(), b.length()) - (a.length() - 1 - al)) {
    if (a.length() > b.length()) {cout << 0 << '\n';}
    else {cout << b.length() - a.length() << '\n';}
  }
  else {cout << b.length() - s - (a.length() - 1 - al) << '\n';}

  return 0;
}