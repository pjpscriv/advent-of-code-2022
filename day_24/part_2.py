BLIZ_DIRECTIONS = [ "^", ">", "v", "<" ]

def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def lowest_common_multiple(a, b):
    return abs(a * b) // greatest_common_divisor(a, b)

class Blizzard:
    x = 0
    y = 0
    direction = ""
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

class Valley():
    width = 1
    height = 1
    grid = []
    blizzards = []
    positions = {}
    minutes = 0
    loop_time = 0

    start = (0, -1)
    end = (0, -1)

    def __init__(self, lines):
        self.height = len(lines) - 2
        self.width = len(lines[0]) - 3
        self.minutes = 0
        self.loop_time = lowest_common_multiple(self.width, self.height)

        for y in range(1, self.height+1):
            for x in range(1, self.width+1):
                v = lines[y][x]
                if v == ".":
                    continue
                if v in BLIZ_DIRECTIONS:
                    self.blizzards.append(Blizzard(x-1, y-1, v))
        
        self.start = (0, -1)
        self.end = (self.width - 1, self.height)
        self.positions[0] = [ self.start ]

    def tick(self):
        for b in self.blizzards:
            if b.direction == "^":
                b.y = b.y - 1 if b.y > 0 else self.height - 1
            elif b.direction == ">":
                b.x = b.x + 1 if b.x < self.width - 1 else 0
            elif b.direction == "v":
                b.y = b.y + 1 if b.y < self.height - 1 else 0 
            elif b.direction == "<":
                b.x = b.x - 1 if b.x > 0 else self.width - 1
        self.minutes += 1

    def navigate(self, goal):
        blizzard_positions = [(b.x, b.y) for b in self.blizzards]

        first_loop_positions = []
        if (self.minutes > self.loop_time):
            first_loop_minutes = self.minutes % self.loop_time
            first_loop_positions = self.positions.get(first_loop_minutes, [])

        last_round = self.minutes - 1
        new_positions = set()

        for p in self.positions[last_round]:
            (x, y) = p
            new_positions = new_positions.union({
                (x, y),     # wait
                (x, y - 1), # up
                (x + 1, y), # right
                (x, y + 1), # down
                (x - 1, y)  # left
            })

            # Check if end position is reached
            if goal in new_positions:
                break

        new_positions = list(new_positions)

        # Filter out invalid positions
        new_positions = [
            (x, y) for x, y in new_positions
            if ((0 <= x < self.width) and (0 <= y < self.height)) or (x, y) == self.start or (x, y) == self.end
        ]

        # Filter out positions with blizzards
        new_positions = [
            (x, y) for x, y in new_positions
            if (x, y) not in blizzard_positions
        ]

        # Filter out paths that have already been fully explored
        new_positions = [
            (x, y) for x, y in new_positions
            if (x, y) not in first_loop_positions
        ]

        self.positions[self.minutes] = new_positions
    
    def print_blizzards(self, include_positions=False):
        print(f"Minute: {self.minutes}")

        blizzard_map = {}
        for b in self.blizzards:
            pos = blizzard_map.get((b.x, b.y), None)
            if pos == None:
                blizzard_map[(b.x, b.y)] = b.direction
            elif pos in BLIZ_DIRECTIONS:
                blizzard_map[(b.x, b.y)] = 2
            else:
                blizzard_map[(b.x, b.y)] = int(pos) + 1
        
        for y in range(-1, self.height + 1):
            for x in range(-1, self.width + 1):
                if (x, y) == self.start or (x, y) == self.end:
                    print(".", end="")
                    continue
                
                if 0 > x or x > self.width-1 or 0 > y or y > self.height-1:
                    print("#", end="")
                    continue

                pos = blizzard_map.get((x, y), ".")
                print(pos, end="")
            print()

        if (include_positions):
            print(f"{len(valley.positions[valley.minutes])} positions")
        
        print()

# Load in grid
with open('input.txt') as f:
    lines = f.readlines()

valley = Valley(lines)

print(f"Start: {valley.start}")
print(f"End: {valley.end}")
print(f"Loop time: {valley.loop_time}")
print()

# Go to the goal
goal = valley.end
while goal not in valley.positions[valley.minutes] and len(valley.positions[valley.minutes]) > 0:
    valley.tick()
    valley.navigate(valley.end)
    print(f"{valley.minutes} - {len(valley.positions[valley.minutes])} positions")

run_1 = valley.minutes
print(f"Got to the end in minutes: {run_1}")
input("Press Enter to continue...\n")

# Go back to the start
valley.minutes = 0
valley.positions = {}
valley.positions[valley.minutes] = [valley.end]
goal = valley.start
while goal not in valley.positions[valley.minutes] and len(valley.positions[valley.minutes]) > 0:
    valley.tick()
    valley.navigate(valley.start)
    print(f"{valley.minutes} - {len(valley.positions[valley.minutes])} positions")

run_2 = valley.minutes
print(f"Got back to the start in minutes: {run_2}")
input("Press Enter to continue...\n")

# Go back to the goal
valley.minutes = 0
valley.positions = {}
valley.positions[valley.minutes] = [valley.start]
goal = valley.end
while goal not in valley.positions[valley.minutes] and len(valley.positions[valley.minutes]) > 0:
    valley.tick()
    valley.navigate(valley.end)
    print(f"{valley.minutes} - {len(valley.positions[valley.minutes])} positions")

run_3 = valley.minutes
print(f"Got back to the end in minutes: {run_3}")
print(f"Done! Completed in a total of minutes: {run_1 + run_2 + run_3}")
