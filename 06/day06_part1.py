input = open("day06_input.txt").read().split('\n')
elements = [line.split() for line in input]

total = 0

for i in range(0, len(elements[0])):
    if elements[4][i] == '*':
        total += int(elements[0][i]) * int(elements[1][i]) * int(elements[2][i]) * int(elements[3][i])
    else:
        total += int(elements[0][i]) + int(elements[1][i]) + int(elements[2][i]) + int(elements[3][i])

print(total)