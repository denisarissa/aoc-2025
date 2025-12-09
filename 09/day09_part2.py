input = open("day09_input.txt").read().split()

edges = []
for i in range(len(input)):
    x1, y1 = int(input[i].split(',')[0]), int(input[i].split(',')[1])
    x2, y2 = int(input[(i + 1) % len(input)].split(',')[0]), int(input[(i + 1) % len(input)].split(',')[1])
    edges.append((x1, y1, x2, y2))

max_area = 0
for i in range(len(input)):
    for j in range(i + 1, len(input)):
        t1, t2 = input[i], input[j]
        x1, y1 = int(t1.split(',')[0]), int(t1.split(',')[1])
        x2, y2 = int(t2.split(',')[0]), int(t2.split(',')[1])
        
        if x1 == x2 or y1 == y2:
            continue
        
        rx_min, rx_max = min(x1, x2), max(x1, x2)
        ry_min, ry_max = min(y1, y2), max(y1, y2)
        
        valid = True
        for ex1, ey1, ex2, ey2 in edges:
            if ex1 == ex2:
                if rx_min < ex1 < rx_max:
                    ey_min, ey_max = min(ey1, ey2), max(ey1, ey2)
                    if not (ey_max <= ry_min or ey_min >= ry_max):
                        valid = False
                        break
            else:
                if ry_min < ey1 < ry_max:
                    ex_min, ex_max = min(ex1, ex2), max(ex1, ex2)
                    if not (ex_max <= rx_min or ex_min >= rx_max):
                        valid = False
                        break
        
        if valid:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            max_area = area if area > max_area else max_area

print(max_area)