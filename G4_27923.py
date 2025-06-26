import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
mList = list(map(int, input().split()))
tList = list(map(int, input().split()))
cList = [0] * (n+1)

for t in tList:
  cList[t-1] += 1
  if (t-1+l < n): cList[t-1+l] -= 1
for i in range(1, n):
  cList[i] += cList[i-1]

cList.sort(reverse=True)
mList.sort(reverse=True)

ans = 0
for i in range(n):
  c = 0
  ans += mList[i] // (1 << cList[i])

print(ans)