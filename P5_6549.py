import sys
input = sys.stdin.readline

n = int(input())
numList = list(input().strip().split())

numList.sort(key=lambda x: x*10, reverse=True)
print(int(''.join(numList)))