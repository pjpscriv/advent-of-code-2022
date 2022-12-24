from math import inf

class Rock():
    def __init__(self, line):
        corners = [(int(x), int(y)) for x, y in [p.split(',') for p in line.split(' -> ')]]
        i = 0
        edges = []
        while i < (len(corners) - 1):
            orig = corners[i]
            dest = corners[i+1]

            # vertical line
            if orig[0] == dest[0]:
                x = orig[0]
                y_min = min(orig[1], dest[1])
                y_max = max(orig[1], dest[1])
                for y in range(y_min+1, y_max):
                    edges.append((x, y))

            # horizontal line
            if orig[1] == dest[1]:
                y = orig[1]
                x_min = min(orig[0], dest[0])
                x_max = max(orig[0], dest[0])
                for x in range(x_min+1, x_max):
                    edges.append((x, y))
            i += 1

        self.points = corners + edges
        x_points = [p[0] for p in self.points]
        y_points = [p[1] for p in self.points]
        self.x_min, self.x_max = min(x_points), max(x_points)
        self.y_min, self.y_max = min(y_points), max(y_points)



with open('input.txt') as f:
    lines = f.readlines()


y_min, y_max = 0, 0
x_min, x_max = inf, 0


rocks = []
for line in lines:
    new_rock = Rock(line.strip())

    if new_rock.y_max > y_max:
        y_max = new_rock.y_max

    if new_rock.x_max > x_max:
        x_max = new_rock.x_max

    if new_rock.x_min < x_min:
        x_min = new_rock.x_min

    rocks.append(new_rock)


# print(f'x: {x_min}, {x_max}')
# print(f'y: {y_min}, {y_max}')

spaces = set([p for r in rocks for p in r.points])

rocks_full = False
sand_count = 0
while not rocks_full:
    sand_point = [500, 0]
    x, y = sand_point

    while True:
        if y > y_max:
            rocks_full = True
            break
        elif (x, y+1) not in spaces:
            y += 1
        elif (x-1, y+1) not in spaces:
            x, y = x-1, y+1
        elif (x+1, y+1) not in spaces:
            x, y = x+1, y+1
        else:
            spaces.add((x, y))
            sand_count += 1
            # print(f'Added sand {sand_count}: {(x, y)}')
            break

print(sand_count)


