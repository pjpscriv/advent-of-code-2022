class Sensor():
    def __init__(self, line):
        x_split = line.split('x=')
        y_split = line.split('y=')
        self.x = int(x_split[1].split(',')[0])
        self.y = int(y_split[1].split(':')[0])
        beacon_x = int(x_split[-1].split(',')[0])
        beacon_y = int(y_split[-1])
        self.beacon = (beacon_x, beacon_y)
        self.beacon_distance = self.get_distance(self.beacon[0], self.beacon[1])

    def __repr__(self):
        return f'({self.x},{self.y}) -> B:{self.beacon}   '

    def get_distance(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def get_y_range(self):
        return (self.y - self.beacon_distance, self.y + self.beacon_distance)

    def get_x_range(self):
        return (self.x - self.beacon_distance, self.x + self.beacon_distance)

    def within_range(self, x, y):
        distance = self.get_distance(x, y)
        return distance <= self.beacon_distance

    def get_x_range_for_y(self, y):
        y_range = self.get_y_range()
        if y_range[0] < y < y_range[1]:
            diff = self.beacon_distance - abs(self.y - y)
            return (self.x - diff, self.x + diff)
        else:
            return ()


def overlaps(a1, a2):
    low = (a2[0]-1) <= a1[0] and a1[0] <= (a2[1]+1)
    top = (a2[0]-1) <= a1[1] and a1[1] <= (a2[1]+1)
    return low or top

def merge(a1, a2):
    return (min(a1[0], a2[0]), max(a1[1], a2[1]))


def ranges_merge(ranges, new):
    new_ranges = []
    for r in ranges:
        if overlaps(r, new) or overlaps(new, r):
            new = merge(r, new)
        else:
            new_ranges.append(r)
    new_ranges.append(new)
    return new_ranges


with open('input.txt') as f:
    lines = f.readlines()


sensors = []
beacons = set()
for line in lines:
    sensor = Sensor(line.strip())
    sensors.append(sensor)
    beacons.add(sensor.beacon)
sensor_points = set([(s.x, s.y) for s in sensors])

xy_min = 0
xy_max = 4000000


# y_ranges = [y for s in sensors for y in s.get_y_range()]
# x_ranges = [x for s in sensors for x in s.get_x_range()]
# x_min = min(x_ranges)
# x_max = max(x_ranges)
# y_min = min(y_ranges)
# y_max = max(y_ranges)

# Print Sensors
# for s in sensors:
#     print(f'{(s.x, s.y)} -> {s.beacon}  :  {s.beacon_distance}')

# Takes ~ 4 minutes
rs = {}
for y in range(xy_max):
    if y % 100000 == 0:
        print('Y point:', y)

    x_ranges = []
    for s in sensors:
        new_range = s.get_x_range_for_y(y)
        # print('   ', new_range)
        if len(new_range) > 0:
            # print('New: ', new_range)
            x_ranges = ranges_merge(x_ranges, new_range)
            # print('  = ', x_ranges)
    rs[y] = x_ranges

    # Print sensor ranges
    if len(x_ranges) > 1:
        print(f'Row {y} - ranges: {x_ranges}')


# Print Range
# for yn in range(xy_max):
#     for xn in range(xy_max):
#         thing = '.'
#         if (xn, yn) in sensor_points:
#             thing = 'S'
#         elif (xn, yn) in beacons:
#             thing = 'B'
#         else:
#             for r in rs[yn]:
#                 if r[0] <= xn <= r[1]:
#                     thing = '#'
#         print(thing, end="")
#     print()


