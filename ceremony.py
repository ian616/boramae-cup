# pylint: skip-file
from itertools import permutations

stage_num, soldier_num = [int(i) for i in input().split(' ')]
min_array = [int(i) for i in input().split(' ')]
prefer_map = [[int(i) for i in input().split(' ')][1:] for _ in range(soldier_num)]

def check_possible(order):
  stage_setting = [[] for _ in range(stage_num)]
  seleted_soldier = []

  for stage in order:
    for soldier in range(soldier_num):
      if not soldier in seleted_soldier:
        for prefer in prefer_map[soldier]:
          if prefer == stage:
            stage_setting[stage-1].append(soldier)
            seleted_soldier.append(soldier)
  
  for i in range(stage_num):
     if min_array[i] > len(stage_setting[i]):
        return False
  return True
        
temp_arr = [i+1 for i in range(stage_num)]

def backtrack(start):
    if start == stage_num:
        if check_possible(temp_arr):
          for i in temp_arr:
              print(i)
          return

    for i in range(start, stage_num):
        temp_arr[start], temp_arr[i] = temp_arr[i], temp_arr[start]
        backtrack(start + 1)
        temp_arr[start], temp_arr[i] = temp_arr[i], temp_arr[start]

backtrack(0)