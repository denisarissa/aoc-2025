input = open("day03_input.txt").read().split('\n')
output = 0

for bank in input:
    num = []
    pos = 0
    
    while len(num) < 12:
        need = 12 - len(num)
        left = len(bank) - pos
        skip = left - need
        
        best_pos = pos
        
        for j in range(pos, pos + skip + 1):
            best_pos = j if bank[j] > bank[best_pos] else best_pos
        
        num.append(bank[best_pos])
        pos = best_pos + 1
    
    output += int(''.join(num))

print(output)