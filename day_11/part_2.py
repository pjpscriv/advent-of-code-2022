from math import floor, prod

ops_dict = {
    'old * 19': lambda x: x * 19,
    'old + 6': lambda x: x + 6,
    'old * old': lambda x: x ** 2,
    'old + 3': lambda x: x + 3,
    'old * 2': lambda x: x * 2,
    'old + 2': lambda x: x + 2,
    'old * 11': lambda x: x * 11,
    'old + 7': lambda x: x + 7,
    'old + 1': lambda x: x + 1,
    'old + 5': lambda x: x + 5,
}


class Monkey():
    id = 0
    items = []
    operation = None
    divisor = 1
    true_m_id = 0
    false_m_id = 0
    inspected = 0

    def parse(self, lines, i):
        self.inspected = 0
        line = lines[i].strip()
        while line != '':
            if line.startswith('Monkey'):
                self.id = int(line.strip(':').split(' ')[-1])
            elif line.startswith('Starting items'):
                item_list = line.split(':')[-1]
                self.items = [int(it.strip()) for it in item_list.split(',')]
            elif line.startswith('Operation'):
                thing = line.split('=')[-1].strip()
                self.operation = ops_dict[thing]
            elif line.startswith('Test'):
                self.divisor = int(line.split(' ')[-1])
            elif line.startswith('If true'):
                self.true_m_id = int(line.split(' ')[-1])
            elif line.startswith('If false'):
                self.false_m_id = int(line.split(' ')[-1])
            i += 1
            line = lines[i].strip() if i < len(lines) else ''
        i += 1
        return i

    def __repr__(self):
        s = ''
        s += f'M{self.id}\n'
        s += f'  it: {self.items}\n'
        s += f'  op: {self.operation}\n'
        s += f'  dv: {self.divisor}\n'
        s += f'  tr: {self.true_m_id}, fl: {self.false_m_id}\n'
        return s

    def inspect(self, monkeys, max_divisor):

        items = self.items
        for worry in items:
            new_worry = self.operation(worry)
            new_worry = new_worry % max_divisor

            if new_worry % self.divisor == 0:
                next_monkey = monkeys[self.true_m_id]
            else:
                next_monkey = monkeys[self.false_m_id]

            next_items = next_monkey.items
            next_items.append(new_worry)
            next_monkey.items = next_items
            self.inspected += 1

        self.items = []


with open('input.txt') as f:
    lines = f.readlines()



monkeys = {}
i = 0
while i < len(lines):
    m = Monkey()
    i = m.parse(lines, i)
    monkeys[m.id] = m


round_count = 10000

max_divisor = prod([m.divisor for m in monkeys.values()])

for r in range(round_count):
    for id in monkeys.keys():
        m = monkeys[id]
        m.inspect(monkeys, max_divisor)


for id in monkeys.keys():
    m = monkeys[id]
    print(f'Monkey {m.id}: {m.inspected} inspections')


inspections = [m.inspected for m in monkeys.values()]
t = sorted(inspections)


print(prod(t[-2:]))
