input = open("day07_input.txt").read().split('\n')

for r in range(len(input)):
    if 'S' in input[r]:
        beams = [(r, input[r].index('S'))]
        break

seen = set()
splits = 0

while beams:
    r, c = beams.pop(0)
    
    if not (0 <= r < len(input) and 0 <= c < len(input[0])):
        continue
    
    if (r, c) in seen:
        continue
    seen.add((r, c))
    
    cell = input[r][c]
    
    if cell == '^':
        splits += 1
        beams.append((r + 1, c - 1))
        beams.append((r + 1, c + 1))
    elif cell == '.' or cell == 'S':
        beams.append((r + 1, c))

print(splits)