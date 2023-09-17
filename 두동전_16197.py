# pylint: skip-file

import sys
from collections import deque

input = sys.stdin.readline

N, M = [int(i) for i in input().split(' ')]
board_status = [list(input()[:-1]) for _ in range(N)]

coin_queue = deque()

temp = []
for i in range(N):
  for j in range(M):
    if board_status[i][j] == 'o':
      temp.append((i, j))

coin_queue.append([temp[0], temp[1], 0])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():

  while not len(coin_queue) == 0:

    (y1, x1), (y2, x2), count = coin_queue.popleft()

    if count >= 10:
      return -1
    
    for i in range(4):
      new_x1 = x1 + dx[i]
      new_x2 = x2 + dx[i]
      new_y1 = y1 + dy[i]
      new_y2 = y2 + dy[i]

      if 0 <= new_x1 < M and 0 <= new_y1 < N and 0 <= new_x2 < M and 0 <= new_y2 < N:

        if board_status[new_y1][new_x1] == '#':
          new_x1 = x1
          new_y1 = y1
        if board_status[new_y2][new_x2] == '#':
          new_x2 = x2
          new_y2 = y2

        coin_queue.append([(new_y1, new_x1), (new_y2, new_x2), count+1])

      elif 0 <= new_x1 < M and 0 <= new_y1 < N:
        return count + 1
      elif 0 <= new_x2 < M and 0 <= new_y2 < N:
        return count + 1
      else:
        continue

print(bfs())