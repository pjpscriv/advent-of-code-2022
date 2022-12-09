class Action():
    direction = ''
    amount = 0

    def __init__(self, line):
        parts = line.strip().split(' ')
        self.direction = parts[0]
        self.amount = int(parts[1])


    def move(self, head, tail, t_history):
        c_head = head
        c_tail = tail

        # move up
        if self.direction == 'U':
            for _ in range(self.amount):
                if (c_head.y > c_tail.y):
                    c_tail.x = c_head.x
                    c_tail.y = c_head.y
                c_head.y = c_head.y + 1
                t_history.append((c_tail.x, c_tail.y))


        # move right
        if self.direction == 'R':
            for _ in range(self.amount):
                if (c_head.x > c_tail.x):
                    c_tail.x = c_head.x
                    c_tail.y = c_head.y
                c_head.x = c_head.x + 1
                t_history.append((c_tail.x, c_tail.y))


        # move left
        if self.direction == 'L':
            for _ in range(self.amount):
                if (c_head.x < c_tail.x):
                    c_tail.x = c_head.x
                    c_tail.y = c_head.y
                c_head.x = c_head.x - 1
                t_history.append((c_tail.x, c_tail.y))

        # move down
        if self.direction == 'D':
            for _ in range(self.amount):
                if (c_head.y < c_tail.y):
                    c_tail.x = c_head.x
                    c_tail.y = c_head.y
                c_head.y = c_head.y - 1
                t_history.append((c_tail.x, c_tail.y))

        return (c_head, c_tail, t_history)



class Knot():
    x = 0
    y = 0

    def __init__(self):
        x = 0
        y = 0



with open('input.txt') as f:
    lines = f.readlines()


actions = []
for line in lines:
    actions.append(Action(line))



# starting state
head = Knot()
tail = Knot()
t_history = []
t_history.append((tail.x, tail.y))

for a in actions:   head, tail, t_history = a.move(head, tail, t_history)





print(len(set(t_history)))

