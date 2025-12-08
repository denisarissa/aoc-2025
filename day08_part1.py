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

connections_attempted = 0
connections_made = 0

for distance, point_a, point_b in edges:
    if connections_attempted >= 1000:
        break
    connections_attempted += 1
    
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

all_circuit_sizes = []
seen_roots = set()
for i in range(total_points):
    root = i
    while parent[root] != root:
        root = parent[root]
    
    if root not in seen_roots:
        seen_roots.add(root)
        all_circuit_sizes.append(circuit_size[root])

all_circuit_sizes.sort(reverse=True)

answer = all_circuit_sizes[0] * all_circuit_sizes[1] * all_circuit_sizes[2]
print(answer)