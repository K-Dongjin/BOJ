#include <cstdio>
#include <set>
using namespace std;

int main() {
  int N, Q, q, i, pos{0}, cnt{0};
  set<int> s;
  scanf("%d %d", &N, &Q);

  int *A = new int[N];
  for (int j=0; j<N; j++) {
    scanf("%d", &A[j]);
    if (A[j] == 1) {
      s.insert(j);
      cnt++;
    }
  }

  for (int j=0; j<Q; j++) {
    scanf("%d", &q);
    if (q == 1) {
      scanf("%d", &i);
      if (A[i-1] == 0) {
        A[i-1] = 1;
        s.insert(i-1);
        cnt++;
      }
      else {
        A[i-1] = 0;
        s.erase(i-1);
        cnt--;
      }
    }
    else if (q == 2) {
      scanf("%d", &i);
      pos = (pos + i) % N;
    }
    else {
      if (cnt > 0) {
        auto it = s.lower_bound(pos);
        if (it != s.end()) {printf("%d\n",*it - pos);}
        else {printf("%d\n", N - (pos - *s.begin()));}
      }
      else {printf("%d\n", -1);}
    }
  }

  return 0;
}


/*
1. 이분 탐색 트리(BST): <set> 헤더의 std::set 클래스 템플릿 사용.
2. 시간 단축: cin/cout 보다 scanf/printf 가 입/출력량이 많아질수록 차이가 심함.
3. 문자열 수가 고정이 아닐 때(Qurey 입력), line20~ 같이 처리 가능.
*/