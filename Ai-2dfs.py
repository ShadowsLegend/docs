graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H', 'I'],
    'E': ['B', 'J'],
    'F': ['C', 'K', 'L'],
    'G': ['C', 'M'],
    'H': ['D'],
    'I': ['D'],
    'J': ['E'],
    'K': ['F'],
    'L': ['F'],
    'M': ['G']
    }
start = 'A'
visited = set()
queue = [start]
print(f'The dfs traversal is: ')
while(queue):
    current = queue[0]
    neighbours = graph[current]
    print(f'{current}', end='->')
    visited.add(current)
    queue.remove(current)
    for neighbour in neighbours:
        if neighbour not in visited:
            queue.insert(0, neighbour)
            visited.add(neighbour)
print(f'End')
