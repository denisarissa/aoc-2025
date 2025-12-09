input = open("day07_input.txt").read().split('\n')

for r in range(len(input)):
    if 'S' in input[r]:
        start_pos = (r, input[r].index('S'))
        break

seen = {start_pos: 1}
splits = 0

for row in range(start_pos[0], len(input)):
    positions = [(r, c) for r, c in seen.keys() if r == row]
    
    for r, c in positions:
        count = seen[(r, c)]
        cell = input[r][c]
        
        if cell == '^':
            if r + 1 < len(input):
                if c - 1 >= 0:
                    seen[(r + 1, c - 1)] = seen.get((r + 1, c - 1), 0) + count
                if c + 1 < len(input[0]):
                    seen[(r + 1, c + 1)] = seen.get((r + 1, c + 1), 0) + count
        elif cell == '.' or cell == 'S':
            if r + 1 < len(input):
                seen[(r + 1, c)] = seen.get((r + 1, c), 0) + count

for (r, c), count in seen.items():
    if r == len(input) - 1:
        splits += count

print(splits)