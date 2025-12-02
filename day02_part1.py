input = open("day02_input.txt").read().split(',')

total = 0
lists = []

for ranges in input:
    first_id = ranges.split('-')[0]
    last_id = ranges.split('-')[1]
    
    len_f = len(first_id)
    len_l = len(last_id)
    
    for length in range(len_f, len_l + 1):
        if length % 2 == 0:

            if length == len_f:
                start = first_id[:int(length/2)]

                if int(str(start) + str(start)) < int(first_id):
                    start = str(int(start) + 1)
            else:
                start = str(pow(10, int(length/2)-1))
            
            limiter = ("9"*length if length < len_l else last_id)
            limiter_end = limiter[:int(length/2)]
            
            for compare in range(int(start), int(limiter_end)+1):
                full_num = int(str(compare)+str(compare))
                if full_num >= int(first_id) and full_num <= int(last_id):
                    total += full_num

print(total)