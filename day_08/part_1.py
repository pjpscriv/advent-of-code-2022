class Tree:
    north_visible = True
    east_visible = True
    south_visible = True
    west_visible = True

    def __init__(self, height, x, y):
        self.height = height
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x},{self.y})'

    def is_visible(self):
        return self.north_visible or self.east_visible or self.south_visible or self.west_visible



with open('input.txt') as f:
    lines = f.readlines()


grid = []
for y in range(len(lines)):
    line = lines[y].strip()
    tree_row = []
    for x in range(len(line)):
        h = int(line[x])
        tree_row.append(Tree(h, x, y))
    grid.append(tree_row)



def set_visibility(tree, grid):
    x, y = tree.x, tree.y

    # North
    y -= 1
    while y >= 0:
        if grid[y][x].height >= tree.height:
            tree.north_visible = False
            break
        y -= 1
    y = tree.y

    # East
    x += 1
    while x <= 98:
        if grid[y][x].height >= tree.height:
            tree.east_visible = False
            break
        x += 1
    x = tree.x

    # South
    y += 1
    while y <= 98:
        if grid[y][x].height >= tree.height:
            tree.south_visible = False
            break
        y += 1
    y = tree.y

    # West
    x -= 1
    while x >= 0:
        if grid[y][x].height >= tree.height:
            tree.west_visible = False
            break
        x -= 1
    x = tree.x


count = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        tree = grid[y][x]
        set_visibility(tree, grid)
        if tree.is_visible():
            count += 1


for row in grid:
    print(''.join([('#' if t.is_visible() else '.') for t in row]))


print(count)
