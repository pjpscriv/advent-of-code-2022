class Node:
    name = ''
    is_dir = True
    parent = None
    size = 0
    children = []

    def __init__(self, name, is_dir, parent, size=0):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self.size = size
        self.children = []

    def get_child_names(self):
        return [c.name for c in self.children]

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise Exception(f'Couldn\'t find child {name} for {self.name}')

    def get_size(self):
        if not self.is_dir and self.size > 0:
            return self.size

        return sum([n.get_size() for n in self.children])

    def get_dir_sizes(self, min_size):
        sizes = []
        self_size = self.get_size()
        if self.is_dir and self_size > min_size:
            sizes.append(self_size)

        dir_children = [n for n in self.children if n.is_dir]

        for c in dir_children:
            sizes += c.get_dir_sizes(min_size)

        return sizes


with open('input.txt') as f:
    lines = f.readlines()



root = Node('/', True, None)
current_node = root
for line in lines:

    if line.startswith('$'):
        parts = line.strip().split(' ')
        if parts[1] == 'ls':
            pass

        elif parts[1] == 'cd':
            destination = parts[2]
            if destination == '..':
                current_node = current_node.parent

            elif destination in current_node.get_child_names():
                current_node = current_node.get_child(destination)

            elif destination == '/':
                current_node = root

    else:
        parts = line.strip().split(' ')

        name = parts[1]
        children = current_node.children

        if not name in current_node.get_child_names():
            if parts[0] == 'dir':
                new_node = Node(name, True, current_node)

            elif parts[0].isnumeric():
                new_node = Node(name, False, current_node, int(parts[0]))

            else:
                raise Exception('The file isn\'t the right format')

            children.append(new_node)
            current_node.children = children


available = 70000000 - root.get_size()
needed = 30000000 - available
print(min(root.get_dir_sizes(needed)))

