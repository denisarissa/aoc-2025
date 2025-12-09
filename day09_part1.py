input = open("day09_input.txt").read().split()

max_area = 0
for i in range(len(input)):
    for j in range(i + 1, len(input)):
        t1, t2 = input[i], input[j]
        area = (abs(int(t2.split(',')[0]) - int(t1.split(',')[0])) + 1) * (abs(int(t2.split(',')[1]) - int(t1.split(',')[1])) + 1)
        
        max_area = area if area > max_area else max_area

print(max_area)