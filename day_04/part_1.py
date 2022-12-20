class Pair():
    e1 = []
    e2 = []

    def __init__(self, line):
        l = line.strip().split(',')
        e1 = l[0].split('-')
        e2 = l[1].split('-')
        self.e1 = [int(e1[0]), int(e1[1])]
        self.e2 = [int(e2[0]), int(e2[1])]

    def fully_contained(self):
        e2_in_e1 = self.e1[0] <= self.e2[0] and self.e2[1] <= self.e1[1]
        e1_in_e2 = self.e2[0] <= self.e1[0] and self.e1[1] <= self.e2[1]
        return e2_in_e1 or e1_in_e2


with open('input.txt') as f:
    lines = f.readlines()


pairs = []
for line in lines:
    pairs.append(Pair(line))

containings = [ (1 if p.fully_contained() else 0) for p in pairs]

print(sum(containings))
