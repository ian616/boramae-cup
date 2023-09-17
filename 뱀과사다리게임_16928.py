# pylint: skip-file

from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(15000)

ladder_num, snake_num = [int(i) for i in input().split(' ')]

ladder_list = [[int(i) for i in input().split(' ')] for _ in range(ladder_num)]
snake_list = [[int(i) for i in input().split(' ')] for _ in range(snake_num)]

visited = [False for _ in range(100)]

def bfs():

  dice = deque()
  dice.append([1, 0])
  min_count = 10000

  while True:
    location, count = dice.popleft()

    if location == 100:
      if min_count > count:
        min_count = count
      break
    
    for i in range(1, 7):
      next = location + i

      for ladder in ladder_list:
        if next == ladder[0]:
          next = ladder[1]

      for snake in snake_list:
        if next == snake[0]:
          next = snake[1]

      if next <= 100 and not visited[next-1]:
        dice.append([next, count + 1])
        visited[next-1] = 1

  print(min_count)
bfs()