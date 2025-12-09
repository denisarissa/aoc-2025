input = open("day04_input.txt").read().split('\n')

rolls = set()
for row in range(0, len(input)):
    for col in range(0, len(input[row])):
        if input[row][col] == '@':
            rolls.add((row, col))

direction = [(-1, 0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1), (-1,-1)]

total = 0
while True:
    can_access = set()
    
    for row, col in rolls:
        adjacent = 0
        for dir_row, dir_col in direction:
            if (row + dir_row, col + dir_col) in rolls:
                adjacent += 1
        
        if adjacent < 4:
            can_access.add((row, col))
    
    if len(can_access) == 0:
        break
    
    rolls -= can_access
    total += len(can_access)

print(total)