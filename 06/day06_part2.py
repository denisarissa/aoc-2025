input = open("day06_input.txt").read().split('\n')
input.insert(0, input.pop())

total = 0
n = []

for i in range(len(input[0]) - 1, -1, -1):
    number = (input[1][i] + input[2][i] + input[3][i] + input[4][i]).strip()
    if number:
        n.append(int(number))
    
    if input[0][i] in '*+':
        result = sum(n) if input[0][i] == '+' else 1
        if input[0][i] == '*':
            for num in n:
                result *= num
        total += result
        n = []

print(total)