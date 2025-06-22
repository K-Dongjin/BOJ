import sys
input = sys.stdin.readline

def manhattans(a, b):
  return abs(a[1] - b[1]) + abs(a[2] - b[2])

n, t = map(int, input().split())
pList = [(-1, -1, -1)]
scList = []
for _ in range(n):
  s, x, y = map(int, input().split())
  pList.append( (s, x, y) )
  if (s == 1): scList.append( (1, x, y) )

for _ in range(int(input())):
  a, b = map(int, input().split())

  ans = manhattans(pList[a], pList[b])
  if ((pList[a][0] == 1) and (pList[b][0] == 1)):
    ans = min(ans, t)

  elif (pList[a][0] == 1):
    for sc in scList:
      temp = t + manhattans(sc, pList[b])
      ans = min(ans, temp)

  elif (pList[b][0] == 1):
    for sc in scList:
        temp = manhattans(pList[a], sc) + t
        ans = min(ans, temp)

  else:
    idxA, idxB = 0, 0
    disA, disB = 2001, 2001
    for i in range(1, n+1):
      if (pList[i][0] == 1):
        temp = manhattans(pList[a], pList[i])
        if (temp < disA):
          disA = temp
          idxA = i
        
        temp = manhattans(pList[i], pList[b])
        if (temp < disB):
          disB = temp
          idxB = i

    if (idxA and idxB and (idxA != idxB)):
      temp = disA + t + disB
      ans = min(ans, temp)

  print(ans)