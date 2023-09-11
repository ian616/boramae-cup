# pylint: skip-file
total = int(input())
word_list = [input() for _ in range(total)]
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

alphabet_group=[]
for word in word_list:
  for alphabet in word:
    if (alphabet in alphabet_list) and not (alphabet in alphabet_group):
      alphabet_group.append(alphabet)
kind_num = len(alphabet_group)

def calculate(digit_list):
  num_list = []
  for word in word_list:
    new_word = []
    for alphabet in word:
      new_word.append(digit_list[alphabet_list.index(alphabet)])
    new_word = [str(i) for i in new_word]
    num_list.append(int(''.join(new_word)))
  return sum(num_list)

result = []

def solve(count, res):
  if count == kind_num:
    result.append(calculate(res))
    return

  for i in range(10-kind_num, 10):
    if not i in res:
      new_list = [j for j in res]
      new_list[count] = i
      solve(count+1, new_list)

solve(0, [-1 for _ in range(10)])
print(max(result))