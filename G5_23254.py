import sys
import heapq as hq
input = sys.stdin.readline

n, m = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

time = 0
heap = []
ans = 0

# 최대 힙 생성(파이썬의 기본은 최소 힙이라 음수화 하여 최대 힙 구현)
for i in range(m):
  hq.heappush(heap, [-bList[i], aList[i]])

while (n*24 > time) and heap:
  b, a = hq.heappop(heap)
  
  if ((100-a) // (-b) <= n*24 - time):
    temp = a + ((-b) * ((100-a) // (-b)))

    if (temp == 100): ans += 100
    else: hq.heappush(heap, [-(100-temp), temp])

    time += (100-a) // (-b)
  
  else:
    ans += a + (n*24 - time) * (-b)
    time += n * 24 - time

for b, a in heap:
  ans += a

print(ans)