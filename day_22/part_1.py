with open('input.txt') as f:
    lines = f.readlines()


def parse_steps(line):
    i = 0
    steps = []
    while i < len(line):
        if i+1 < len(line) and line[i+1].isnumeric():
            steps.append(int(line[i:i+2]))
            if len(line) > i+2:
                steps.append(line[i+2])
                i += 1
            i += 2
        else:
            steps.append(int(line[i]))
            if i+1 < len(line):
                steps.append(line[i+1])
                i += 1
            i += 1
    return steps


def get_next_pos(board, pos, facing):
    y, x = pos
    next_y, next_x = y, x
    if facing == 0: # Right
        next_x = x + 1
    elif facing == 1: # Down
        next_y = y + 1
    elif facing == 2: # Left
        next_x = x - 1
    else: # Up
        next_y = y - 1

    max_y = len(board)
    max_x = len(board[0])
    next = ' '
    if 0 <= next_y < max_y and 0 <= next_x < max_x:
        next = board[next_y][next_x]

    if next == ' ':
        i = 1
        if facing == 0:
            while x - i >= 0 and board[y][x - i] != ' ':
                i += 1
            next_x = x - i + 1
        elif facing == 1:
            while y - i >= 0 and board[y - i][x] != ' ':
                i += 1
            next_y = y - i + 1
        elif facing == 2:
            while x + i < max_x and board[y][x + i] != ' ':
                i += 1
            next_x = x + i - 1
        else:
            while y + i < max_y and board[y + i][x] != ' ':
                i += 1
            next_y = y + i - 1

    return (next_y, next_x)


def forward(board, pos, facing):
    next_pos = get_next_pos(board, pos, facing)
    next = board[next_pos[0]][next_pos[1]]
    if next == '#':
        return pos
    if next == '.':
        return next_pos


def password(pos, facing):
    return ((pos[0] + 1) * 1000) + ((pos[1] + 1) * 4) + facing


board = []
max_len = max([len(l) - 1 for l in lines[:-2]])
for l in lines[:-2]:
    row = list(l.strip('\n'))
    row += [' '] * (max_len - len(row))
    board.append(row)

steps = parse_steps(lines[-1].strip())


pos = (0, board[0].index('.'))
facing = 0

for step in steps:
    if step in ['L', 'R']:
        turn = 1 if step == 'R' else -1
        facing = (facing + turn) % 4
    else:
        for _ in range(step):
            pos = forward(board, pos, facing)


print(password(pos, facing))
