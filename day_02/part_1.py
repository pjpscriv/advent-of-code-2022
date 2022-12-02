
score_map = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

# opponent
# A for Rock
# B for Paper
# C for Scissors

# me
# X for Rock
# Y for Paper
# Z for Scissors

# Score
# 0 if you lost
# 3 if the round was a draw
# 6 if you won

win_map = {
    'X': { # Rock
        'A': 3,
        'B': 0,
        'C': 6
    },
    'Y': { # Paper
        'A': 6,
        'B': 3,
        'C': 0
    },
    'Z': { # Scissors
        'A': 0,
        'B': 6,
        'C': 3
    }
}

class Game():
    opponent = ''
    me = ''
    score = 0

    def __init__(self, line):
        pair = line.strip().split(' ')
        self.opponent = pair[0]
        self.me = pair[1]
        self.score = score_map[self.me] + win_map[self.me][self.opponent]



with open('input.txt') as f:
    lines = f.readlines()



scores = []
for line in lines:
    scores.append(Game(line).score)

print(sum(scores))
