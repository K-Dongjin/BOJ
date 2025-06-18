import sys
input = sys.stdin.readline

cost = 10000
stockDic = {}
for _ in range(int(input())):
  p, x, f = map(int, input().split()) #p: 가격, x: 물량, f: 판매(-1)/구매(1)
  
  if p not in stockDic: stockDic[p] = x * f
  else:
    if (stockDic[p] * f < 0):
      cost = p
    stockDic[p] += x * f

print(cost)