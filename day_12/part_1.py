from math import inf


class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = []
        self.distance = inf
        self.neighbours = []

    def __repr__(self):
        return f'Node ({self.x},{self.y})\n  N: {self.neighbours}'


def get_key(x, y):
    return f'({x}, {y})'


def get_level(val):
    if val.islower():
        return ord(val) - 97
    elif val == 'E':
        return 25
    return 0


def parse_node(lines, x, y, nodes):
    key = get_key(x, y)

    y_max = len(lines)
    x_max = len(lines[0].strip())

    level = get_level(lines[y][x])
    node = Node(x, y)
    nodes[key] = node

    possible = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    neighbours = [(x, y) for x, y in possible if (0 <= x < x_max and 0 <= y < y_max)]

    for x_new, y_new in neighbours:
        new_level = get_level(lines[y_new][x_new])
        new_key = get_key(x_new, y_new)
        if new_level <= level + 1 and not new_key in node.neighbours:
            node.neighbours += [new_key]

    return node


def get_next_node(nodes):
    distances = [(n.distance, get_key(n.x, n.y)) for n in [nodes[n] for n in nodes]]
    distances.sort()
    return nodes[distances[0][1]]


with open('input.txt') as f:
    lines = f.readlines()


# Load nodes
nodes = {}
for i in range(len(lines[0].strip())):
    for j in range(len(lines)):
        parse_node(lines, i, j, nodes)


# Get start & end
start_key, end_key = (None, None)
for y, line in enumerate(lines):
    if 'S' in line:
        start_key = get_key(line.index('S'), y)
    if 'E' in line:
        end_key = get_key(line.index('E'), y)
    if start_key and end_key:
        break
start = nodes[start_key]
end = nodes[end_key]
start.distance = 0


# Do path finding - takes about a minute
node = start
while end.distance == inf:
    # print(f'Visit {get_key(node.x, node.y)}')

    for key in node.neighbours:
        if key in nodes.keys():
            new_node = nodes[key]
            new_distance = node.distance + 1
            new_path = node.path + [get_key(node.x, node.y)]

            if new_distance < new_node.distance:
                new_node.distance = new_distance
                new_node.path = new_path
                nodes[key] = new_node

    del nodes[get_key(node.x, node.y)]
    node = get_next_node(nodes)


print(end.path)
print(end.distance)

