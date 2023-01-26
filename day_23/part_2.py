def get_directions(round, loc):
    dir = round % 4
    if dir == 0:
        return [(loc[0]-1, loc[1]-1), (loc[0], loc[1]-1), (loc[0]+1, loc[1]-1)]
    elif dir == 1:
        return [(loc[0]-1, loc[1]+1), (loc[0], loc[1]+1), (loc[0]+1, loc[1]+1)]
    elif dir == 2:
        return [(loc[0]-1, loc[1]-1), (loc[0]-1, loc[1]), (loc[0]-1, loc[1]+1)]
    else:
        return [(loc[0]+1, loc[1]-1), (loc[0]+1, loc[1]), (loc[0]+1, loc[1]+1)]


def surroundings_are_empty(loc, locs):
    surrounds = [
        (loc[0]-1, loc[1]-1),
        (loc[0]-1, loc[1]),
        (loc[0]-1, loc[1]+1),
        (loc[0],   loc[1]-1),
        (loc[0],   loc[1]+1),
        (loc[0]+1, loc[1]-1),
        (loc[0]+1, loc[1]),
        (loc[0]+1, loc[1]+1)
    ]
    return not any([(s in locs) for s in surrounds])


def get_next_location(loc, locs, r):
    if surroundings_are_empty(loc, locs):
        return loc
    for i in range(r, r+4):
        check_locs = get_directions(i, loc)
        if not any((c in locs) for c in check_locs):
            return check_locs[1]
    return loc


def print_locs(locs):
    x_vals = [l[0] for l in locs]
    y_vals = [l[1] for l in locs]
    for y in range(min(y_vals+[0]), max(y_vals+[12])+1):
        for x in range(min(x_vals+[0]), max(x_vals+[14])+1):
            if (x, y) in locs:
                print('#', end="")
            else:
                print('.', end="")
        print()
    print()


# Get elf positions
with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]


elf_locations = set()
for y, line in enumerate(lines):
    for x in range(len(line)):
        if lines[y][x] == '#':
            elf_locations.add((x, y))


# print_locs(elf_locations)


# Takes about 10 sec
r = 0
proposed_moves = {}
while len(proposed_moves) > 0 or r < 1:

    proposed_moves = {}
    for loc in elf_locations:
        proposed = get_next_location(loc, elf_locations, r)
        if proposed != loc:
            proposed_moves[proposed] = proposed_moves.get(proposed, []) + [loc]

    for dest, srcs in proposed_moves.items():
        if len(srcs) == 1:
            elf_locations.remove(srcs[0])
            elf_locations.add(dest)

    r += 1

    # print(f"    {r} :  -> {len(proposed_moves)}")
    # if r in [1,2,3,4,5,10]:
    #     print(f'== End of Round {r} ==')
    #     print_locs(elf_locations)



print(r)
# print_locs(elf_locations)

