# pylint: skip-file
import sys

input = sys.stdin.readline
sys.setrecursionlimit(15000)

total = int(input())
sequence = list(map(int, input().split(' ')))

sum_list = []
for i in range(2**total):
  bits = bin(i)[2:]

  if len(bits) < total:
    bits = '0' * (total - len(bits)) + bits
  
  temp = [int(bits[i])*sequence[i] for i in range(total)]
  sum_list.append(sum(temp))

sum_list = set(sum_list)
sum_list = list(sum_list)
sum_list.sort()

is_found = False
for i in range(len(sum_list)):
  if i != sum_list[i]:
    is_found = True
    print(i)
    break

if not is_found:
  print(sum_list[-1]+1)
