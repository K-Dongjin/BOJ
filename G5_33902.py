import sys
input = sys.stdin.readline

mList = []
for _ in range(int(input())):
  s, e = map(int, input().split())
  mList.append( (s, e) )

mList.sort(key=lambda x: (x[1], x[0]))

endTime = 0
ans = 0
for s, e in mList:
  if (endTime <= s):
    ans += 1
    endTime = e

print(ans)