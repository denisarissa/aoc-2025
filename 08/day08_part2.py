input = open("day08_input.txt").read()
points = []
for line in input.strip().split('\n'):
    if line:
        x, y, z = line.split(',')
        points.append((int(x), int(y), int(z)))

total_points = len(points)

edges = []
for i in range(total_points):
    for j in range(i + 1, total_points):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        dz = points[i][2] - points[j][2]
        distance = (dx**2 + dy**2 + dz**2)**0.5
        edges.append((distance, i, j))

edges.sort()

parent = list(range(total_points))
circuit_size = [1] * total_points

last_connected_pair = None
connections_made = 0

for distance, point_a, point_b in edges:
    
    root_a = point_a
    while parent[root_a] != root_a:
        parent[root_a] = parent[parent[root_a]]
        root_a = parent[root_a]
    
    root_b = point_b
    while parent[root_b] != root_b:
        parent[root_b] = parent[parent[root_b]]
        root_b = parent[root_b]
    
    if root_a != root_b:
        parent[root_b] = root_a
        circuit_size[root_a] += circuit_size[root_b]
        connections_made += 1
        last_connected_pair = (point_a, point_b)
                
        if circuit_size[root_a] == total_points:
            break

point_a_index = last_connected_pair[0]
point_b_index = last_connected_pair[1]

point_a_coords = points[point_a_index]
point_b_coords = points[point_b_index]

x_coordinate_a = point_a_coords[0]
x_coordinate_b = point_b_coords[0]

answer = x_coordinate_a * x_coordinate_b
print(answer)