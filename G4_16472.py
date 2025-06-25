import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()

dic = {}
ans = 1
kind = 0
s, e = 0, -1
flag = True
while (e < len(string) - 1):
  e += 1
  alpE = string[e]

  if alpE in dic: dic[alpE] += 1
  else: dic[alpE] = 1

  if (dic[alpE] == 1): kind += 1

  if (kind <= n): ans = max(ans, e-s+1)
  else:
    while (True):
      alpS = string[s]
      dic[alpS] -= 1
      s += 1
      if (dic[alpS] == 0):
        kind -= 1
        break

print(ans)