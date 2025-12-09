input = open("day04_input.txt").read().split('\n')

rolls = set()
for row in range(0, len(input)):
    for col in range(0, len(input[row])):
        if input[row][col] == '@':
            rolls.add((row, col))

can_access = 0
direction = [(-1, 0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1), (-1,-1)]

for row, col in rolls:
    adjacent = 0
    for dir_row, dir_col in direction:
        if (row+dir_row, col+dir_col) in rolls:
            adjacent += 1
    if adjacent < 4:
        can_access += 1

print(can_access)