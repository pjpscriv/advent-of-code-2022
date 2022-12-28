def rock_height(chamber):
    i = -1
    while not '#' in chamber[i]:
        i -= 1
    return len(chamber) + i

def rock_shape(i, h):
    if i == 0: # bar
        return [(2,h), (3,h), (4,h), (5,h)]
    elif i == 1: # cross
        return [(2,h+1), (3,h), (3,h+1), (3,h+2), (4,h+1)]
    elif i == 2: # backwards L
        return [(2,h), (3,h), (4,h), (4,h+1), (4,h+2)]
    elif i == 3: # pipe
        return [(2,h), (2,h+1), (2,h+2), (2,h+3)]
    elif i == 4: # square
        return [(2,h), (2,h+1), (3,h), (3,h+1)]

def move(shape, x_move, y_move=0):
    for x, _ in shape:
        if not (0 <= (x+x_move) < 7):
            return shape
    return [(x+x_move,y+y_move) for x,y in shape]

def can_move(shape, chamber, x_move, y_move=0):
    for x,y in shape:
        if not (0 <= (x+x_move) < 7):
            return False
        if chamber[y+y_move][x+x_move] == '#':
            return False
    return True

def add_shape(chamber, shape):
    for (x,y) in shape:
        chamber[y][x] = '#'
    return chamber

def print_chamber(chamber):
    for i in range(len(chamber)):
        print(''.join(chamber[(i+1)*-1]))


with open('input.txt') as f:
    wind = f.readline().strip()

chamber = [['#'] * 7] + [[' '] * 7 for _ in range(4)]


count = 0
wind_time = 0
while count < 2022:
    h = rock_height(chamber) + 4
    max_rock = h + 4
    s = rock_shape(count % 5, h)

    if len(chamber) < max_rock:
        empty_layers = [[' '] * 7 for _ in range((max_rock - len(chamber)))]
        chamber = chamber + empty_layers

    rock_falling = True
    while rock_falling:

        w = wind[wind_time % len(wind)]
        if w == '<' and can_move(s, chamber, -1):
            s = move(s, -1)
        elif w == '>' and can_move(s, chamber, 1):
            s = move(s, 1)
        wind_time += 1

        if can_move(s, chamber, 0, -1):
            s = move(s, 0, -1)
        else:
            chamber = add_shape(chamber, s)
            rock_falling = False

    count += 1


print(rock_height(chamber))

