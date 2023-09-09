# pylint: skip-file

y_len, x_len = [int(i) for i in input().split(' ')]
poster_map = [list(input()) for _ in range(y_len)]
is_possible = True

def draw_map():
    # 테두리에 파란색부분 채우기
    for i in range(y_len):
        for j in range(x_len):
            if (i == 0 or j == 0 or i == (y_len-1) or j == (x_len-1)):
                poster_map[i][j] = 'B'

    # 중앙에 노란색부분 채우기
    for i in range(y_len):
        if 0 < i < (y_len-1):
            if poster_map[i][(x_len-1) // 2] == 'X':
                poster_map[i][(x_len-1) // 2] = 'Y'
            if poster_map[i][(x_len) // 2] == 'X':
                poster_map[i][(x_len) // 2] = 'Y'

    # 나머지에 흰색부분 채우기
    for i in range(y_len):
        for j in range(x_len):
            if poster_map[i][j] == 'X':
                poster_map[i][j] = 'W'

# 조건에 부합하는지 확인
def check_first_rule():
    global is_possible
    is_all_blue = True

    for i in range(y_len):
        if poster_map[i][(x_len-1) // 2] == 'W' or poster_map[i][(x_len) // 2] == 'W':
            is_possible = False
        elif poster_map[i][(x_len-1) // 2] == 'Y' or poster_map[i][(x_len) // 2] == 'Y':
            is_all_blue = False

    if is_all_blue:
        is_possible = False

def check_second_rule():
    global is_possible
    is_no_white = True

    for i in range(y_len):
        for j in range(x_len):
            if poster_map[i][j] != poster_map[i][x_len-j-1]:
                is_possible = False
            if poster_map[i][j] == 'W':
                is_no_white = False
    if is_no_white:
        is_possible = False

# 결과 출력
def print_result():
    if is_possible:
        print('YES')
        for i in poster_map:
            for j in i:
                print(j, end='')
            print('')
    else:
        print('NO')

draw_map()
check_first_rule()
check_second_rule()
print_result()
