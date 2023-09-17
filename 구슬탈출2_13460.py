# pylint: skip-file
import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(15000)

N, M = [int(i) for i in input().split(' ')]
board = [list(input()[:-1]) for _ in range(N)]

red_location = ()
blue_location = ()

for i in range(N):
  for j in range(M):
    if board[i][j] == 'R':
      red_location = (i, j)
    elif board[i][j] == 'B':
      blue_location = (i, j)

status_queue = deque()

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

def bfs():
  global status_queue

  while len(status_queue):
    red, blue, count = status_queue.popleft()

    if count == 10:
      return -1
    
    for i in range(4):
      new_red =  red
      new_blue = blue

      red_blocked = False
      blue_blocked = False
      can_append = True

      end = False
      while True:
        if (not (0 <= new_red[0] < N and 0 <= new_red[1] < M)) or (not (0 <= new_blue[0] < N and 0 <= new_blue[1] < M)):
          break
        
        new_red = (new_red[0] + dy[i], new_red[1] + dx[i])
        new_blue = (new_blue[0] + dy[i], new_blue[1] + dx[i])

        if board[new_red[0]][new_red[1]] == '#':
          red_blocked = True
          new_red = (new_red[0] - dy[i], new_red[1] - dx[i])

          if new_red == new_blue and not end:
            new_blue = (new_blue[0] - dy[i], new_blue[1] - dx[i])
            break

        if board[new_blue[0]][new_blue[1]] == '#':
          blue_blocked = True
          new_blue = (new_blue[0] - dy[i], new_blue[1] - dx[i])
          if new_red == new_blue and not end:
            new_red = (new_red[0] - dy[i], new_red[1] - dx[i])
            break

        if red_blocked and blue_blocked:
          break

        if board[new_red[0]][new_red[1]] == 'O':
          end = True

        if board[new_blue[0]][new_blue[1]] == 'O':
          end = False
          can_append = False
          break
        
      if end:
        return count+1 
      
      if can_append:
        status_queue.append([new_red, new_blue, count+1])

status_queue.append([red_location, blue_location, 0])
print(bfs())
          
