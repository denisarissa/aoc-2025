input = open("day02_input.txt").read().split(',')

total = 0
lists = []

for ranges in input:
    first_id = ranges.split('-')[0]
    last_id = ranges.split('-')[1]
    
    len_f = len(first_id)
    len_l = len(last_id)
    
    for length in range(len_f, len_l + 1):
        for pattern_len in range(1, int(length/2) + 1):
            if length % pattern_len == 0:
                num_repeats = int(length / pattern_len)

                if length == len_f:
                    start = first_id[:pattern_len]
                    test_num = int(str(start) * num_repeats)
                    if test_num < int(first_id):
                        start = str(int(start) + 1)
                else:
                    start = str(pow(10, pattern_len-1)) if pattern_len > 1 else "1"

                limiter = ("9"*length if length < len_l else last_id)
                limiter_end = limiter[:pattern_len]
                
                for compare in range(int(start), int(limiter_end)+1):
                    full_num = int(str(compare) * num_repeats)
                    if full_num >= int(first_id) and full_num <= int(last_id):
                        if str(full_num) not in lists:
                            total += full_num
                            lists.append(str(full_num))

print(total)