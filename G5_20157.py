import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
ans = 0
pgDic = {"INF": 0}
ngDic = {"INF": 0}

for _ in range(n):
  x, y = map(int, input().split())
  if (x == 0):
    if (y > 0): pgDic["INF"] += 1
    else: ngDic["INF"] += 1
    ans = max(ans, pgDic["INF"], ngDic["INF"])
  else:
    g = gcd(x, y)
    grad = (x//g, y//g)
    if (y > 0):
      if grad in pgDic: pgDic[grad] += 1
      else: pgDic[grad] = 1
      ans = max(ans, pgDic[grad])
    else:
      if grad in ngDic: ngDic[grad] += 1
      else: ngDic[grad] = 1
      ans = max(ans, ngDic[grad])

print(ans)