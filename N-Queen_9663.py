# pylint: skip-file

import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)

N = int(input())

board = [-1 for _ in range(N)]

method_count = 0

def check_possible(i, count):
  for n in range(count):
    if board[n] == i:
      return False
    if abs(n-count) == abs(board[n] - i):
      return False
  return True
    

def solve(count):
  global board, method_count

  if count == N:
    method_count += 1
    return
  
  for i in range(N):
    if check_possible(i, count):
      board[count] = i
      solve(count+1)
      board[count] = 0

solve(0)
print(method_count)