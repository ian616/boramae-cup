# pylint: skip-file

import sys

input = sys.stdin.readline
sys.setrecursionlimit(15000)


sudoku_map = [[int(i) for i in input().split(' ')] for _ in range(9)]

def is_possible(i, j, num):
  for n in range(9):
    if sudoku_map[i][n] == num or sudoku_map[n][j] == num:
      return False
    
  box_y = (i // 3) * 3
  box_x = (j // 3) * 3
  for n in range(3):
    for m in range(3):
      if sudoku_map[box_y+n][box_x+m] == num:
        return False
  
  return True

zero_index = []
for n in range(9):
  for m in range(9):
    if sudoku_map[n][m] == 0:
      zero_index.append((n, m))

is_found = False
def dfs(count):
  global is_found

  if is_found: return
  if count == len(zero_index):
    is_found = True
    for i in sudoku_map:
      for j in i:
        print(j, end=' ')
      print()
      
    return
  
  i, j = zero_index[count]

  for n in range(1, 10):
    if is_possible(i, j, n):
      sudoku_map[i][j] = n
      dfs(count+1)
      sudoku_map[i][j] = 0

dfs(0)