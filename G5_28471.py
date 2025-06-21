import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [ list(input().rstrip()) for _ in range(n) ]

for i in range(n):
  for j in range(n):
    if (board[i][j] == 'F'):
      y, x = i, j
      break

dy = [-1, -1, -1, 0, 0, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 1]
dq = deque( [(y, x)] )
cnt = 0

while (dq):
  cy, cx = dq.popleft()

  for i in range(7):
    ny, nx = cy + dy[i], cx + dx[i]
    if ((0 <= ny < n) and (0 <= nx < n) and (board[ny][nx] == '.')):
      board[ny][nx] = 'v'
      cnt += 1
      dq.append((ny, nx))

print(cnt)