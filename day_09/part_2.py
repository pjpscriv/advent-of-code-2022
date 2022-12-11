class Action():
    direction = ''
    amount = 0

    def __init__(self, line):
        parts = line.strip().split(' ')
        self.direction = parts[0]
        self.amount = int(parts[1])


    def move(self, rope, t_history):
        for _ in range(self.amount):
            tail_pos = rope.move(self.direction)
            p_tuple = (tail_pos.x, tail_pos.y)
            if not p_tuple in t_history:
                t_history.append(p_tuple)

        return (rope, t_history)


class Knot():
    name = ''
    x = 0
    y = 0
    def __init__(self, name):
        self.name = 'H' if name == 0 else name
        self.x = 0
        self.y = 0


class Rope():
    segments = []

    def __init__(self, length):
        self.segments = [Knot(i) for i in range(length)]


    def move(self, direction):
        if direction == 'U':
            self.move_segment(0, 0, 1)
        if direction == 'R':
            self.move_segment(0, 1, 0)
        if direction == 'L':
            self.move_segment(0, -1, 0)
        if direction == 'D':
            self.move_segment(0, 0, -1)
        return self.segments[-1]


    def __repr__(self):
        x = [k.x for k in self.segments]
        y = [k.y for k in self.segments]

        min_x = min(min(x), 0)
        max_x = max(x)
        min_y = min(min(y), 0)
        max_y = max(y)

        grid = []
        for _ in range(min_y, max_y+1):
            row = []
            for _ in range(min_x, max_x+1):
                row.append('.')
            grid.append(row)

        for s in self.segments:
            grid[s.y - min_y][s.x - min_x] = f'{s.name}'

        out = ''
        for line in grid:
            l = ''.join(line)
            out = f'{l}\n{out}'

        return out


    def move_segment(self, index, dx, dy):
        head = self.segments[index]

        if index < len(self.segments) - 1:
            tail = self.segments[index+1]

            p_dx = head.x - tail.x
            p_dy = head.y - tail.y

            dx_t = 0
            dy_t = 0

            # Same position
            if p_dx == 0 and p_dy == 0:
                pass

            # Diagonal position
            elif abs(p_dx) + abs(p_dy) > 1:
                if p_dx == dx or (dx == 0 and p_dy == dy):
                    dx_t = p_dx

                if p_dy == dy or (dy == 0 and p_dx == dx):
                    dy_t = p_dy

            # Normal position
            else:
                if p_dx == dx or (p_dx == 0 and p_dy == dy):
                    dx_t = dx

                if p_dy == dy or (p_dy == 0 and p_dx == dx):
                    dy_t = dy

            if dx_t != 0 or dy_t != 0:
                self.move_segment(index+1, dx_t, dy_t)

        head.x = head.x + dx
        head.y = head.y + dy




with open('input.txt') as f:
    lines = f.readlines()


actions = []
for line in lines:
    actions.append(Action(line))


rope = Rope(10)


t_history = []
t_history.append((0, 0))


for a in actions:
    rope, t_history = a.move(rope, t_history)
    print(a.direction, a.amount)
    print(rope)


print(len(set(t_history)))

