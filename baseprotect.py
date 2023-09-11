# pylint: skip-file
import math

total_jinbub, train_day, day_jinbub, N, M= [int(i) for i in input().split(' ')]
jinbub_map = [[[int(i) for i in input().split(' ')] for _ in range(N)] for _ in range(total_jinbub)]
diff_graph = [[ 0 for _ in range(total_jinbub)] for _ in range(total_jinbub)]
last_jinbub = [int(i)-1 for i in input().split(' ')]

# 두 진법 사이의 피로도 계산
def get_diff(map1, map2):
  total_diff = 0
  for i in range(N):
    for j in range(M):
      if map1[i][j] != map2[i][j]:
        total_diff += 1
  return total_diff**2

#피로도 맵 생성
for i in range(total_jinbub):
  for j in range(total_jinbub):
    diff_graph[i][j] = get_diff(jinbub_map[i], jinbub_map[j])

# 두 점 사이의 최소 피로도 구하기
def get_minimum(jinbub1, jinbub2):
  path = [0 for _ in range(day_jinbub-1)]
  path.append(jinbub2)
  path.insert(0, jinbub1)

  minimum = math.inf
  for n in range(day_jinbub-1):
    for m in range(total_jinbub):
      total = 0
      path[n+1] = m
      for i in range(day_jinbub):
        total += diff_graph[path[i]][path[i+1]]
      if minimum > total:
        minimum = total

  return minimum

# 최소 피로도 구하기
last_jinbub.insert(0, 0)
total_diff = 0
for i in range(train_day):
  if day_jinbub == 1:
    total_diff += diff_graph[last_jinbub[i]][last_jinbub[i+1]]
  else:
    total_diff += get_minimum(last_jinbub[i], last_jinbub[i+1])

print(total_diff)

