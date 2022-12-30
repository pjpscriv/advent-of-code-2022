with open('input.txt') as f:
    lines = f.readlines()


drops = [tuple([int(p) for p in l.strip().split(',')]) for l in lines]
dim_ranges = {
    'x': [min([d[0] for d in drops]), max([d[0] for d in drops])],
    'y': [min([d[1] for d in drops]), max([d[1] for d in drops])],
    'z': [min([d[2] for d in drops]), max([d[2] for d in drops])],
}
d_set = set(drops)

space = {}
for x in range(dim_ranges['x'][0] - 1, dim_ranges['x'][1] + 2):
    plane = {}
    for y in range(dim_ranges['y'][0] - 1, dim_ranges['y'][1] + 2):
        z_row = {}
        for z in range(dim_ranges['z'][0] - 1, dim_ranges['z'][1] + 2):
            z_row[z] = '#' if (x,y,z) in d_set else '.'
        plane[y] = z_row
    space[x] = plane


area = 0
for dx, dy, dz in drops:
    neighbours = [
        space[dx+1][dy][dz],
        space[dx-1][dy][dz],
        space[dx][dy+1][dz],
        space[dx][dy-1][dz],
        space[dx][dy][dz+1],
        space[dx][dy][dz-1]
    ]
    area += neighbours.count('.')

print(area)
