class Tree:
    north_view_distance = 0
    east_view_distance = 0
    south_view_distance = 0
    west_view_distance = 0

    def __init__(self, height, x, y):
        self.height = height
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x},{self.y})'

    def scenic_score(self):
        return self.north_view_distance * self.east_view_distance * self.south_view_distance * self.west_view_distance



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
        tree.north_view_distance += 1
        if grid[y][x].height >= tree.height:
            break
        y -= 1
    y = tree.y

    # East
    x += 1
    while x <= 98:
        tree.east_view_distance += 1
        if grid[y][x].height >= tree.height:
            break
        x += 1
    x = tree.x

    # South
    y += 1
    while y <= 98:
        tree.south_view_distance += 1
        if grid[y][x].height >= tree.height:
            break
        y += 1
    y = tree.y

    # West
    x -= 1
    while x >= 0:
        tree.west_view_distance += 1
        if grid[y][x].height >= tree.height:
            break
        x -= 1
    x = tree.x


max_score = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        tree = grid[y][x]
        set_visibility(tree, grid)
        if tree.scenic_score() > max_score:
            max_score =  tree.scenic_score()


for row in grid:
    print(''.join([str(t.scenic_score())[-1] for t in row]))


print(max_score)
