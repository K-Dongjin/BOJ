import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
aList = list(map(int, input().split()))

dq = deque()
for i in range(n):
  if dq and (dq[0][0] <= i-l): dq.popleft()

  while dq and (aList[i] < dq[-1][1]):
    dq.pop()
  
  dq.append( (i, aList[i]) )

  print(dq[0][1], end=' ')


'''73%에서 시간 초과 난거 보니 답은 맞는 듯
import sys
from collections import deque
input = sys.stdin.readline

def findMin(s, e):
  ans = INF
  idx = s - 1
  for i in range(s, e+1):
    if (ans >= aList[i]):
      ans = aList[i]
      idx = i
  return idx

INF = 10**9 + 1

n, l = map(int, input().split())
aList = [INF] * (l-1) + list(map(int, input().split()))
ans = []
s, e, minIdx = -1, l-2, l-2
for _ in range(n):
  s += 1; e += 1
  
  if (minIdx < s): minIdx = findMin(s, e)
  else:
    if (aList[minIdx] >= aList[e]): minIdx = e
  
  print(aList[minIdx], end=' ')
'''