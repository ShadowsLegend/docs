graph = {
  'A': ['B', 'C', 'D'],
  'B': ['A', 'E'],
  'C': ['A', 'E', 'F'],
  'D': ['A', 'F'],
  'E': ['B', 'C', 'H'],
  'F':  ['D', 'C', 'G'],
  'G': ['F', 'H'],
  'H': ['G', 'E']
    }
heuristic = {
    'A': 40,
    'B': 35,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10
    }
start = 'A'
goal = 'G'
visited = set()
visited.add(start)
path = [start]
current = start
while(current!=goal):
    min_cost = 10000
    neighbours = graph[current]
    for neighbour in neighbours:
        cost = heuristic[neighbour]
        if (cost<min_cost and neighbour not in visited):
            min_cost = cost
            best = neighbour
    path.append(best)
    visited.add(best)
    current = best
for node in path:
    print(f'{node}', end='->')
print('Stop')