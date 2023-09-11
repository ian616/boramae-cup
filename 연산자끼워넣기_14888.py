# # pylint: skip-file

# total = int(input())
# num_arr = [int(i) for i in input().split(' ')]
# operator = [int(i) for i in input().split(' ')]

# def caculate(operator_order):

#   def calc_recursive(count, res):
#     if count == total:
#       return res
#     elif count == 0: return calc_recursive(count+1, num_arr[0]) 
#     else:
#       if operator_order[count - 1] == 0:
#         temp = res + num_arr[count]
#       elif operator_order[count - 1] == 1:
#         temp = res - num_arr[count]
#       elif operator_order[count - 1] == 2:
#         temp = res * num_arr[count]
#       elif operator_order[count - 1] == 3:
#         temp = int(res // num_arr[count])
#       return calc_recursive(count+1, temp)

#   return calc_recursive(0, 0)

# result_arr = []

# def solve(count, res, count_arr):

#   if count == total - 1:
#     result_arr.append(caculate(res))
#     return
  
#   for i in range(4):
#     if not count_arr[i] == operator[i]:
#       temp_res = [j for j in res]
#       temp_res.append(i)

#       temp_count_arr = [j for j in count_arr]
#       temp_count_arr[i] += 1

#       solve(count + 1, temp_res, temp_count_arr)

# solve(0, [], [0 for _ in range(4)])
# print(max(result_arr))
# print(min(result_arr))

n = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split());
max_result = - int(1e9)
min_result = int(1e9)

def dfs(add, sub, mul, div, sum, idx):
    global max_result, min_result
    if idx == n:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return
    if add:
        dfs(add-1, sub, mul, div, sum + number[idx], idx + 1)
    if sub:
        dfs(add, sub-1, mul, div, sum - number[idx], idx + 1)
    if mul:
        dfs(add, sub, mul-1, div, sum * number[idx], idx + 1)
    if div:
        dfs(add, sub, mul, div-1, int(sum / number[idx]), idx + 1)
        
dfs(add, sub, mul, div, number[0], 1)
print(max_result)
print(min_result)