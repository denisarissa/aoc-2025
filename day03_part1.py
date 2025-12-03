input = open("day03_input.txt").read().split('\n')
output = 0

for bank in input:
    max_joltage = 0
    max_cur = int(bank[-1])
    
    for i in range(len(bank) - 2, -1, -1):
        digit = int(bank[i])

        max_joltage = max(max_joltage, digit * 10 + max_cur)

        max_cur = max(max_cur, digit)
    output += max_joltage

print(output)