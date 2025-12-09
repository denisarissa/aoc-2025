input = open("day01_input.txt").read().split('\n')

position = 50
password = 0

for rotation in input:
    direction = rotation[0]
    distance = int(rotation[1:])

    if direction == 'L':
        for turn in range(0,distance):
            if position == 0:
                position = 99
            else:
                position -= 1
            if position == 0:
                password += 1
            
    else:
        for turn in range(0,distance):
            if position == 99:
                position = 0
            else:
                position += 1
            if position == 0:
                password += 1

print(password)