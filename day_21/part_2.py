class Monkey():
    def __init__(self, line):
        parts = line.strip().split(': ')
        self.name = parts[0]
        if self.name == 'humn':
            self.value = None
            self.eqn = None
            self.refs = []
        elif parts[1].isnumeric():
            self.value = int(parts[1])
            self.eqn = None
        else:
            self.value = None
            self.eqn = parts[1] if self.name != 'root' else parts[1].replace('+', '=')
            eqn_parts = self.eqn.split(' ')
            self.refs = [eqn_parts[0], eqn_parts[2]]

    def can_eval(self):
        eqn_parts = self.eqn.split(' ')
        return eqn_parts[0].isnumeric() and eqn_parts[2].isnumeric()

    def get_solved(self):
        eqn_parts = self.eqn.split(' ')
        if eqn_parts[0].isnumeric():
            return (int(eqn_parts[0]), 0)
        elif eqn_parts[2].isnumeric():
            return (int(eqn_parts[2]), 1)

    def get_unsolved(self):
        eqn_parts = self.eqn.split(' ')
        if not eqn_parts[0].isnumeric():
            return eqn_parts[0]
        elif not eqn_parts[2].isnumeric():
            return eqn_parts[2]

    def apply_solved(self, value):
        if self.name == 'humn':
            return value

        op = self.eqn.split(' ')[1]
        v, side = self.get_solved()

        if op == '+':
            return value - v
        if op == '*':
            return value // v
        if op == '-' and side == 0:
            return -(value - v)
        if op == '-' and side == 1:
            return value + v
        if op == '/' and side == 0:
            return v // value
        if op == '/' and side == 1:
            return value * v


with open('input.txt') as f:
    lines = f.readlines()


value_found = []
monkeys = {}
referers = {}
for line in lines:
    m = Monkey(line)
    monkeys[m.name] = m
    if m.value:
        value_found.append(m.name)
    else:
        for r in m.refs:
            referers[r] = referers.get(r, []) + [m.name]


while len(value_found) > 0:
    v_name = value_found.pop()
    v_value = monkeys[v_name].value
    for m_name in referers[v_name]:
        m = monkeys[m_name]
        m.eqn = m.eqn.replace(v_name, str(v_value))

        if m.can_eval():
            m.value = int(eval(m.eqn))
            value_found.insert(0, m.name)


current = monkeys['root']
value = current.get_solved()[0]
while current.name != 'humn':
    unsolved = current.get_unsolved()
    # print(f'{unsolved} = {value}')
    next = monkeys[unsolved]
    # print(f'{next.eqn} = {value}')
    value = next.apply_solved(value)
    current = next


print(value)
