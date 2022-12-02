
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
# X for Lose
# Y for Draw
# Z for Win

# Score
# 0 if you lost
# 3 if the round was a draw
# 6 if you won

# 1 for Rock
# 2 for Paper
# 3 for Scissors

win_map = {
    'X': { # Lose
        'A': 3,
        'B': 1,
        'C': 2
    },
    'Y': { # Draw
        'A': 1+3,
        'B': 2+3,
        'C': 3+3
    },
    'Z': { # Win
        'A': 2+6,
        'B': 3+6,
        'C': 1+6
    }
}

class Game():
    opponent = ''
    me = ''
    score = 0

    def __init__(self, line):
        pair = line.strip().split(' ')
        self.opponent = pair[0]
        self.win_lose = pair[1]
        self.score = win_map[self.win_lose][self.opponent]



with open('input.txt') as f:
    lines = f.readlines()



scores = []
for line in lines:
    scores.append(Game(line).score)

print(sum(scores))
