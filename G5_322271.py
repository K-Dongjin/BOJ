import sys
input = sys.stdin.readline

BIGNUM = 10**9

N = int(input())
aList = [0] + list(map(int, input().split()))
aList.sort()

dp = [ [0, 0] for _ in range(500001) ]
dp[1][0], dp[1][1] = BIGNUM, BIGNUM

for i in range(2, N+1):
  if (i % 2 == 0): 
    dp[i][0] = dp[i-2][0] + (aList[i] - aList[i-1])
    dp[i][1] = BIGNUM
  else:
    dp[i][0] = dp[i-2][0] + (aList[i] - aList[i-1])
    dp[i][1] = min(dp[i-2][1] + (aList[i] - aList[i-1]), dp[i-3][0] + (aList[i] - aList[i-2]))

print(dp[N][1])