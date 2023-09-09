# pylint: skip-file

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

# 두 점 사이의 최단경로 구하기
def get_minimum(jinbub1, jinbub2):
  return diff_graph[jinbub1][jinbub2]

# 최소 피로도 구하기
last_jinbub.insert(0, 0)
total_diff = 0
for i in range(train_day):
  total_diff += get_minimum(last_jinbub[i], last_jinbub[i+1])

print(total_diff)

print("__________")
