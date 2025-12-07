input = open("day05_input.txt").read().split('\n\n')
ranges = sorted(input[0].split('\n'), key=lambda x: int(x.split('-')[0]))

fresh = 0
last_high = -1

for cur_r in range(0, len(ranges)):
    low = int(ranges[cur_r].split('-')[0])
    high = int(ranges[cur_r].split('-')[1])
    
    if low <= last_high:
        low = last_high + 1
    
    if high > last_high:
        fresh += high - low + 1
        last_high = high

print(fresh)