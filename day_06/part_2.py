with open('input.txt') as f:
    line = f.readlines()[0].strip()

for i in range(14, len(line)):
    last_four = line[(i-14):i]
    if len(set(last_four)) == 14:
        print(i)
        break
