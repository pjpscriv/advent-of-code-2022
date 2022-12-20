class Group:
    group = []
    e1 = ''
    e2 = ''
    e3 = ''

    def __init__(self, g):
        self.group = g
        self.e1 = g[0]
        self.e2 = g[1]
        self.e3 = g[2]

    def common_char(self):
        for char in self.e1:
            if char in self.e2:
                if char in self.e3:
                    return char

    def __repr__(self):
        return f'{len(self.group)}: \n\t{self.e1}-\n\t{self.e2}-\n\t{self.e3}'



def get_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38



with open('input_2.txt') as f:
    lines = f.readlines()

groups = []

t = 0
group = []
for line in lines:
    l = line.strip()
    if t > 2:
        groups.append(Group(group))
        group = []
        t = 0
    group.append(l)
    t += 1

c = [(x.common_char()) for x in groups]

p = [get_priority(y) for y in c]

print(sum(p))
