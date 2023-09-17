# pylint: skip-file
import sys

input = sys.stdin.readline
sys.setrecursionlimit(15000)

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
board_list = []
domino_list = []

while True:
  domino_num = int(input())
  if domino_num == 0:
    break
  
  board = [[0 for _ in range(9)] for _ in range(9)]
  dominos = []

  for i in range(1, 10):
    for j in range(1, 10):
      if i < j:
        dominos.append([i, j])

  for _ in range(domino_num):
    n, index1, m, index2 = input().split(' ')
    n = int(n)
    m = int(m)
    board[alphabet_list.index(index1[0])][int(index1[1]) - 1] = n
    board[alphabet_list.index(index2[0])][int(index2[1]) - 1] = m

    dominos.remove(sorted((n, m)))

  index_list = input().split(' ')
  for i in range(9):
    index = index_list[i]
    board[alphabet_list.index(index[0])][int(index[1]) - 1] = i + 1

  board_list.append(board)
  domino_list.append(dominos)

# board의 빈칸에 특정 숫자가 들어갈 수 있는지 판단하는 함수
def is_possible(board, i, j, num):
  for n in range(9):
    if board[i][n] == num or board[n][j] == num:
      return False
    
  box_y = (i // 3) * 3
  box_x = (j // 3) * 3
  for n in range(3):
    for m in range(3):
      if board[box_y+n][box_x+m] == num:
        return False
  return True

is_found = False
# 하나의 보드에 대해 실행
def one_board(given_board, given_dominos):
  board = given_board[:]
  dominos = given_dominos[:]
  used_dominos = []

  def find_next():
    for i in range(9):
      for j in range(9):
        if board[i][j] == 0:
          return (i, j)
  
  # dfs로 dominos의 모든 경우를 백트래킹 
  
  def solve(count):
    global is_found
    
    if is_found: return

    if len(dominos) == 0:
      is_found = True
      for k in board:
        for l in k:
          print(l, end='')
        print('')
      return 

    i, j = find_next()
    for n in range(len(dominos)):
      if i < 8:
        if board[i][j] == 0 and board[i+1][j] == 0:

          if is_possible(board, i, j, dominos[n][0]) and is_possible(board, i+1, j, dominos[n][1]):
            board[i][j] = dominos[n][0]
            board[i+1][j] = dominos[n][1]
            temp = dominos.pop(n)
            used_dominos.append(temp)
            solve(count+1)
            board[i][j] = 0
            board[i+1][j] = 0
            dominos.insert(n, temp)
            used_dominos.pop()
          if is_possible(board, i, j, dominos[n][1]) and is_possible(board, i+1, j, dominos[n][0]):
            board[i][j] = dominos[n][1]
            board[i+1][j] = dominos[n][0]
            temp = dominos.pop(n)
            used_dominos.append(temp)
            solve(count+1)
            board[i][j] = 0
            board[i+1][j] = 0
            dominos.insert(n, temp)
            used_dominos.pop()
      
      if j < 8: 
        if board[i][j] == 0 and board[i][j+1] == 0:
          if is_possible(board, i, j, dominos[n][0]) and is_possible(board, i, j+1, dominos[n][1]):
            board[i][j] = dominos[n][0]
            board[i][j+1] = dominos[n][1]
            temp = dominos.pop(n)
            used_dominos.append(temp)
            solve(count+1)
            board[i][j] = 0
            board[i][j+1] = 0
            dominos.insert(n, temp)
            used_dominos.pop()
          if is_possible(board, i, j, dominos[n][1]) and is_possible(board, i, j+1, dominos[n][0]):
            board[i][j] = dominos[n][1]
            board[i][j+1] = dominos[n][0]
            temp = dominos.pop(n)
            used_dominos.append(temp)
            solve(count+1)
            board[i][j] = 0
            board[i][j+1] = 0
            dominos.insert(n, temp)
            used_dominos.pop()
    
  solve(0)
  
for i in range(len(board_list)):
  print('Puzzle '+ str(i+1))
  one_board(board_list[i], domino_list[i])
  is_found = False

