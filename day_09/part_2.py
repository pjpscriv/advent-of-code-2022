class Action():
    direction = ''
    amount = 0

    def __init__(self, line):
        parts = line.strip().split(' ')
        self.direction = parts[0]
        self.amount = int(parts[1])


    def move(self, rope, t_history) -> str:

        for _ in range(self.amount):

            # move up
            if self.direction == 'U':
                for i in range(len(rope) - 1):
                    c_head = rope[i]
                    c_tail = rope[i+1]

                    if (c_head.y > c_tail.y):
                        c_tail.x = c_head.x
                        c_tail.y = c_head.y
                    c_head.y = c_head.y + 1
                    rope[i] = c_head
                    rope[i+1] = c_tail
                t_history.append((c_tail.x, c_tail.y))


            # move right
            if self.direction == 'R':
                for i in range(len(rope) - 1):
                    c_head = rope[i]
                    c_tail = rope[i+1]

                    if (c_head.x > c_tail.x):
                        c_tail.x = c_head.x
                        c_tail.y = c_head.y
                    c_head.x = c_head.x + 1
                    rope[i] = c_head
                    rope[i+1] = c_tail
                t_history.append((c_tail.x, c_tail.y))


            # move left
            if self.direction == 'L':
                for i in range(len(rope) - 1):
                    c_head = rope[i]
                    c_tail = rope[i+1]

                    if (c_head.x < c_tail.x):
                        c_tail.x = c_head.x
                        c_tail.y = c_head.y
                    c_head.x = c_head.x - 1
                    rope[i] = c_head
                    rope[i+1] = c_tail
                t_history.append((c_tail.x, c_tail.y))

            # move down
            if self.direction == 'D':
                for i in range(len(rope) - 1):
                    c_head = rope[i]
                    c_tail = rope[i+1]

                    if (c_head.y < c_tail.y):
                        c_tail.x = c_head.x
                        c_tail.y = c_head.y
                    c_head.y = c_head.y - 1
                    rope[i] = c_head
                    rope[i+1] = c_tail
                t_history.append((c_tail.x, c_tail.y))

            return (rope, t_history)



class Knot():
    name = ''
    x = 0
    y = 0

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0



with open('input.txt') as f:
    lines = f.readlines()


actions = []
for line in lines:
    actions.append(Action(line))




# 284 - too low!!!!


rope = [Knot(i) for i in range(10)]

t_history = []
t_history.append((rope[-1].x, rope[-1].y))


for a in actions:
    rope, t_history = a.move(rope, t_history)




print(len(set(t_history)))

