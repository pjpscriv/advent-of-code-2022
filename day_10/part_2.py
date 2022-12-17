class Op():
    type = ''
    amount = 0

    def __init__(self, line):
        parts = line.strip().split(' ')
        self.type = parts[0]
        if len(parts) > 1:
            self.amount = int(parts[1])


class State():

    def __init__(self):
        self.register = 1
        self.queue = []

    def execute(self, op):
        if op.type == 'addx':
            self.queue.insert(0, 0)
            self.queue.insert(0, op.amount)
        else:
            pass
            self.queue.insert(0, 0)

        self.register += self.queue.pop()

    def execte(self):
        if (len(self.queue) > 0):
            self.register += self.queue.pop()




with open('input.txt') as f:
    lines = f.readlines()


ops = []
for line in lines:
    ops.append(Op(line))


record_cycles = [20, 60, 100, 140, 180, 220]
cycle_sum = 0
state = State()

display =''

i = 1
while i <= len(ops) or len(state.queue) > 0:

    crt_pos = (i - 1) % 40

    if -1 <= (state.register - crt_pos) <= 1:
        display += '#'
    else:
        display += ' '

    if crt_pos == 39:
        display += '\n'

    op = ops[i - 1] if len(ops) >= i else None

    if (i in record_cycles):
        cycle_sum += state.register * i

    if op:
        state.execute(op)
    else:
        state.execte()

    i += 1

print(display)
