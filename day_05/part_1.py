class Action():
    amount = 0
    start = 0
    end = 0

    def __init__(self, line):
        parts = line.strip().split(' ')
        self.amount = int(parts[1])
        self.start = int(parts[3])
        self.end = int(parts[5])


    def act(self, crates):
        start_stack = crates[self.start]
        end_stack = crates[self.end]

        for _ in range(self.amount):
            c = start_stack.pop()
            end_stack.append(c)

        crates[self.start] = start_stack
        crates[self.end] = end_stack

        return crates


crates = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}


with open('input.txt') as f:
    lines = f.readlines()


for line in lines[:8]:
    for i in range(1, 10):
        index = ((i-1)*4) + 1
        if len(line) > index:
            char = line[index].strip()
            if char != '':
                new_list = crates[i]
                new_list.insert(0, char)
                crates[i] = new_list


actions = []
for line in lines[10:]:
    actions.append(Action(line))


for a in actions:
    crates = a.act(crates)

tops = [crates[k][-1] for k in crates.keys()]

print(''.join(tops))
