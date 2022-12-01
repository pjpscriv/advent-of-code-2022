
with open('input.txt') as f:
    lines = f.readlines()


def most_calories(lines):
    all = []
    current = 0
    for line in lines:
        l = line.strip()
        if l == '':
            all.append(current)
            current = 0

        else:
            cal = int(line)
            current += cal
    return all


all_cals = most_calories(lines)

print(max(all_cals))
