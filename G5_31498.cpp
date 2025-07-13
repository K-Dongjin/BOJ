#include <cstdio>
using namespace std;

int power(int base, int exp);
void hanoi(int n, int from, int mid, int to);

int main() {
  int N, t;
  scanf("%d", &N);

  t = power(2, N) - 1;
  printf("%d\n", t);
  hanoi(N, 1, 2, 3);

  return 0;
}

int power(int base, int exp) {
  if (exp == 1) {return base;}
  else {
    int temp = power(base, exp/2);
    if (exp % 2 == 0) {return temp*temp;}
    else {return temp*temp*base;}
  }
}

void hanoi(int n, int from, int mid, int to) {
  if (n == 1) {printf("%d %d\n", from, to);}
  else {
    hanoi(n-1, from, to, mid);
    printf("%d %d\n", from, to);
    hanoi(n-1, mid, from, to);
  }
}