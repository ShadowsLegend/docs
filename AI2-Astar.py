graph = {
    'S': [['A', 1], ['G', 10]],
    'A': [['B', 2], ['C', 1]],
    'B': [['D', 5]],
    'C': [['D', 3], ['G', 4]],
    'D': [['G', 2]],
    'G': []
    }
heuristics = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0
    }
start = 'S'
goal = 'G'
visited = set()
queue = [(start, heuristics[start], [start], 0)]
while(queue):
    queue.sort(key = lambda x:x[1])
    current, estimated_cost, path, actual_cost = queue.pop(0)
    if (current == goal):
        print("The best solution is: ")
        print(f'The path is: {path}')   
        print(f'The cost is: {actual_cost}')
        break
    if (current not in visited):
        visited.add(current)
        neighbours = graph[current]
        for node, edge_cost in neighbours:
            if node not in visited:
                queue.append((node, estimated_cost - heuristics[current] + heuristics[node] + edge_cost, path + [node], actual_cost + edge_cost))
