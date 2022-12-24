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

with open('input.txt') as f:
    lines = f.readlines()


sensors = []
beacons = set()
for line in lines:
    sensor = Sensor(line.strip())
    sensors.append(sensor)
    beacons.add(sensor.beacon)
sensor_points = set([(s.x, s.y) for s in sensors])

y_ranges = [y for s in sensors for y in s.get_y_range()]
x_ranges = [x for s in sensors for x in s.get_x_range()]
x_min = min(x_ranges)
x_max = max(x_ranges)


# Takes about a minute to run
count = 0
y = 2000000
print(f'X range: {(x_min, x_max)} - Size: {abs(x_min-x_max)}')
for x in range(x_min, x_max):
    within = False

    if x % 100000 == 0:
        print('X point:', x)

    if not (x,y) in beacons and not (x,y) in sensor_points:
        for s in sensors:
            if s.within_range(x, y):
                within = True
                break
        if within:
            count += 1


print(count)

