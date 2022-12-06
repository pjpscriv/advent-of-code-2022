with open('input.txt') as f:
    line = f.readlines()[0].strip()

for i in range(4, len(line)):
    last_four = line[(i-4):i]
    if len(set(last_four)) == 4:
        print(i)
        break
