# pylint: skip-file

num = int(input())
stat_map = [[int(i) for i in input().split(' ')] for _ in range(num)]

result_arr = []
def solve(count, res):
  global result_arr
  if count == num:
    result_arr.append(res)
    return

  for i in range(2):
    if res.count(i) < (num / 2):
      new_list = [j for j in res]
      new_list.append(i)
      solve(count + 1, new_list)

solve(0, [])

diff_arr = []
for res in result_arr:
  stat_1 = 0
  stat_2 = 0
  for i in range(num):
    for j in range(num):
      if res[i] == 0 and res[j] == 0:
        stat_1 += stat_map[i][j]
      elif res[i] == 1 and res[j] == 1:
        stat_2 += stat_map[i][j]

  diff_arr.append(abs(stat_1 - stat_2))

print(min(diff_arr))