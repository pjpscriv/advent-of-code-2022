with open('input.txt') as f:
    lines = f.readlines()


zero_key = ''
things = {}
for i, n in enumerate(lines):
    key = f'start-{i}'
    things[key] = [i, int(n), key]
    if int(n) == 0:
        zero_key = key

for key in things.keys():
    index, value, _ = things[key]

    next_i = (index + value) # C H E C K
    next_i = next_i % (len(things)-1)
    low = min(index, next_i)
    high = max(index, next_i)

    updates = [t for t in things.values() if low <= t[0] <= high and t[0] != index]
    move = 1 if next_i < index else -1

    for i, v, k in updates:
        things[k] = [(i + move), v, k]

    things[key] = [next_i, value, key]


start_i = things[zero_key][0]
sorted_things = sorted(things.values())
indicies = [t[0] for t in sorted_things]


vals = [
    sorted_things[(start_i + 1000) % len(things)][1],
    sorted_things[(start_i + 2000) % len(things)][1],
    sorted_things[(start_i + 3000) % len(things)][1]
]

print(sum(vals))
