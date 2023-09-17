# pylint: skip-file

import sys
input = sys.stdin.readline

N, M = [int(i) for i in input().split(' ')]
number_map = [[int(i) for i in input().split(' ')] for _ in range(N)]

max_val = max([max(i) for i in number_map])

max = 0
def solve(count, sum, visited, i, j):
  temp_visited = visited[:]
  global number_map, max

  # if max >= sum + max_val * (3 - count):
  #   return
  
  temp_visited[i][j] = 1

  if count == 3:
    temp =  sum+number_map[i][j]
    if max < temp:
      max = temp
    return

  if i > 0 and not(temp_visited[i-1][j]):
    if count == 1:
      temp_visited[i-1][j] = 1
      solve(count+1, sum+number_map[i-1][j], temp_visited, i, j)
      temp_visited[i-1][j] = 0

    solve(count+1, sum+number_map[i][j], temp_visited, i-1, j)

  if j > 0 and not(temp_visited[i][j-1]):
    if count == 1:
      temp_visited[i][j-1] = 1
      solve(count+1, sum+number_map[i][j-1], temp_visited, i, j)
      temp_visited[i][j-1] = 0

    solve(count+1, sum+number_map[i][j], temp_visited, i, j-1)
  if i < N-1 and not(temp_visited[i+1][j]):
    if count == 1:
      temp_visited[i+1][j] = 1
      solve(count+1, sum+number_map[i+1][j], temp_visited, i, j)
      temp_visited[i+1][j] = 0

    solve(count+1, sum+number_map[i][j], temp_visited, i+1, j)
  if j < M-1 and not(temp_visited[i][j+1]):
    if count == 1:
      temp_visited[i][j+1] = 1
      solve(count+1, sum+number_map[i][j+1], temp_visited, i, j)
      temp_visited[i][j+1] = 0

    solve(count+1, sum+number_map[i][j], temp_visited, i, j+1)

for i in range(N):
  for j in range(M):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    solve(0, 0, visited, i, j)

print(max)



