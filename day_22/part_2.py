mode = 'input'

with open(f'{mode}.txt') as f:
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


if mode == 'input':
    edge_wraps = [
        { 'start': [(49,  0), (49, 49)], 'end': [(0, 149), (0, 100)], 'rot': 2 },
        { 'start': [(50, -1), (99, -1)], 'end': [(0, 150), (0, 199)], 'rot': 1 },
        { 'start': [(100,-1), (149,-1)], 'end': [(0, 199), (49,199)], 'rot': 0 },
        { 'start': [(150, 0), (150,49)], 'end': [(99,149), (99,100)], 'rot': 2 },
        { 'start': [(100,50), (149,50)], 'end': [(99, 50), (99, 99)], 'rot': 1 },
        { 'start': [(49, 50), (49, 99)], 'end': [(0, 100), (49,100)], 'rot': -1 },
        { 'start': [(50,150), (99,150)], 'end': [(49,150), (49,199)], 'rot': 1 },

        { 'start': [(-1, 149), (-1, 100)], 'end': [(50,  0), (50, 49)], 'rot': 2 },
        { 'start': [(-1, 150), (-1, 199)], 'end': [(50,  0), (99,  0)], 'rot': -1 },
        { 'start': [(0,  200), (49, 200)], 'end': [(100, 0), (149, 0)], 'rot': 0 },
        { 'start': [(100,149), (100,100)], 'end': [(149, 0), (149,49)], 'rot': 2 },
        { 'start': [(100, 50), (100, 99)], 'end': [(100,49), (149,49)], 'rot': -1 },
        { 'start': [(0,   99), (49,  99)], 'end': [(50, 50), (50, 99)], 'rot': 1 },
        { 'start': [(50, 150), (50, 199)], 'end': [(50,149), (99,149)], 'rot': -1 }
    ]
else:
    edge_wraps = [
        { 'start': [(7,0),(7,3)], 'end': [(4,4),(7,4)], 'rot': -1 },
        { 'start': [(8,-1),(11,-1)], 'end': [(3,4),(0,4)], 'rot': 2 },
        { 'start': [(12,0),(12,3)], 'end': [(15,11),(15,8)], 'rot': 2 },
        { 'start': [(12,4),(12,7)], 'end': [(15,8),(12,8)], 'rot': 1 },
        { 'start': [(4,8),(7,8)], 'end': [(8,11),(8,8)], 'rot': -1 },
        { 'start': [(0,8),(3,8)], 'end': [(11,11),(8,11)], 'rot': 2 },
        { 'start': [(-1,4),(-1,7)], 'end': [(15,11),(12,11)], 'rot': 1 },

        { 'start': [(4,3),(7,3)], 'end': [(8,0),(8,3)], 'rot': 1 },
        { 'start': [(3,3),(0,3)], 'end': [(8,0),(11,0)], 'rot': 2 },
        { 'start': [(16,11),(16,8)], 'end': [(11,0),(11,3)], 'rot': 2 },
        { 'start': [(15,7),(12,7)], 'end': [(11,4),(11,7)], 'rot': -1 },
        { 'start': [(7,11),(7,8)], 'end': [(4,7),(7,7)], 'rot': 1 },
        { 'start': [(11,12),(8,12)], 'end': [(0,7),(3,7)], 'rot': 2 },
        { 'start': [(15,12),(12,12)], 'end': [(0,4),(0,7)], 'rot': -1 }
    ]


def wrap(x, y, facing):
    for edge in edge_wraps:
        start = edge['start']
        end = edge['end']
        rot = edge['rot']

        if start[0][0] == start[1][0]:
            step = 1 if start[0][1] < start[1][1] else -1
            start_rng = [(start[0][0], sy) for sy in range(start[0][1], start[1][1]+step, step)]
        elif start[0][1] == start[1][1]:
            step = 1 if start[0][0] < start[1][0] else -1
            start_rng = [(sx, start[0][1]) for sx in range(start[0][0], start[1][0]+step, step)]

        if (x, y) in start_rng:
            if end[0][0] == end[1][0]:
                step = 1 if end[0][1] < end[1][1] else -1
                end_rng = [(end[0][0], sy) for sy in range(end[0][1], end[1][1]+step, step)]
            elif end[0][1] == end[1][1]:
                step = 1 if end[0][0] < end[1][0] else -1
                end_rng = [(sx, end[0][1]) for sx in range(end[0][0], end[1][0]+step, step)]

            i = start_rng.index((x, y))
            x, y = end_rng[i]
            facing = (facing + rot) % 4
            return (x, y, facing)

    return (x, y, facing)


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
        next_x, next_y, facing = wrap(next_x, next_y, facing)
        next = board[next_y][next_x]

    return ((next_y, next_x), facing)


def forward(board, pos, facing):
    next_pos, next_facing = get_next_pos(board, pos, facing)
    next = board[next_pos[0]][next_pos[1]]
    if next == '#':
        return (pos, facing)
    if next == '.':
        return (next_pos, next_facing)


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

# print('START', pos, facing)

for step in steps:
    if step in ['L', 'R']:
        turn = 1 if step == 'R' else -1
        facing = (facing + turn) % 4
    else:
        for _ in range(step):
            pos, facing = forward(board, pos, facing)
    # print(step, ':', pos, facing)


print(password(pos, facing))

