import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cList = [ int(input()) for _ in range(n) ]

dp = [0] * (k+1)
dp[0] = 1

for c in cList:
  for i in range(c, k+1):
      dp[i] += dp[i-c]

print(dp[k])