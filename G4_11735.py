import sys
input = sys.stdin.readline

n, q = map(int, input().split())
sigmaN = (n * (n+1)) // 2
sumR, sumC = sigmaN, sigmaN

cngR, cngC = [], []
for _ in range(q):
  rc, line = input().split()
  line = int(line)

  if (rc == 'R'):
    if line in cngR:
      print(0)
      continue
    else:
      print(sumR + line*(n-len(cngC)))
      sumC -= line
      cngR.append(line)

  else:
    if line in cngC:
      print(0)
      continue
    else:
      print(sumC + line*(n-len(cngR)))
      sumR -= line
      cngC.append(line)