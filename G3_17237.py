import sys
input = sys.stdin.readline

n = int(input())
dList = [0] * 21
for _ in range(n):
  dList[int(input())] += 1

for i in range(20, 0, -1):
  dList[i-1] += dList[i] >> 1

print('A' if dList[0] > 0 else 'B')