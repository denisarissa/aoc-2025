input = open("day05_input.txt").read().split('\n\n')
ranges = sorted(input[0].split('\n'), key=lambda x: int(x.split('-')[0]))
ids = sorted([int(i) for i in input[1].split('\n')])

fresh = 0
id_pos = 0

for cur_r in range(0, len(ranges)):
    low = int(ranges[cur_r].split('-')[0])
    high = int(ranges[cur_r].split('-')[1])
    
    while id_pos < len(ids):
        i = ids[id_pos]

        if i > high:
            break
        
        if i >= low and i <= high:
            fresh += 1
        
        id_pos += 1

print(fresh)