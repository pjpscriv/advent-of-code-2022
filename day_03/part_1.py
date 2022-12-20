
class Rucksack():
    c1 = ''
    c2 =''

    def __init__(self, line):
        l = line.strip()
        self.c1 = l[:len(l)//2]
        self.c2 = l[len(l)//2:]

    def __repr__(self):
        return f'{self.c1} : {self.c2}\n'

    def common_char(self):
        for c in self.c1:
            if c in self.c2:
                return c


def get_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


with open('input.txt') as f:
    lines = f.readlines()

rucksacks = []

for line in lines:
    rucksacks.append(Rucksack(line))

l = [get_priority(x.common_char()) for x in rucksacks]

print(sum(l))
