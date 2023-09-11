# pylint: skip-file

total = int(input())
sign_arr = input().split(' ')
result = [0 for _ in range(total+1)]

def possible(num1, num2, sign):
  if sign == '>':
    return num1>num2
  else:
    return num1<num2

result = []
def solve(count, res):
  global result
  if count == total+1:
    result.append(res)
    return
  
  for i in range(10):
    if not i in res:
      if count == 0 or possible(res[count-1], i, sign_arr[count-1]):
        new_list = [j for j in res]
        new_list.append(i)
        solve(count+1, new_list)

solve(0, [])
min, max = [str(i) for i in result[0]], [str(i) for i in result[-1]]
print(''.join(max))
print(''.join(min))