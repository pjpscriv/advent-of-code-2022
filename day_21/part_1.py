class Monkey():
    def __init__(self, line):
        parts = line.strip().split(': ')
        self.name = parts[0]
        if parts[1].isnumeric():
            self.value = int(parts[1])
            self.eqn = None
        else:
            self.value = None
            self.eqn = parts[1]
            eqn_parts = self.eqn.split(' ')
            self.refs = [eqn_parts[0], eqn_parts[2]]

    def can_eval(self):
        eqn_parts = self.eqn.split(' ')
        return eqn_parts[0].isnumeric() and eqn_parts[2].isnumeric()


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


while not monkeys['root'].value :
    v_name = value_found.pop()
    v_value = monkeys[v_name].value
    for m_name in referers[v_name]:
        m = monkeys[m_name]
        m.eqn = m.eqn.replace(v_name, str(v_value))

        if m.can_eval():
            m.value = int(eval(m.eqn))
            value_found.insert(0, m.name)


print(monkeys['root'].value)
