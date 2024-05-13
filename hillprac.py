import random
graph = {
    'S': [['A', 1], ['G', 10]],
    'A': [['B', 2], ['C', 1]],
    'B': [['D', 5]],
    'C': [['D', 3], ['G', 4]],
    'D': [['G', 2]],
    'G': []
    }
start = 'S'
goal = 'G'
def soln(graph, start, goal):
    current = start
    visited = set()
    path=[current]
    t_cost = 0
    count = 0
    while current!=goal and count < 5:
        neighbours = graph[current]
        node, cost = random.choice(neighbours)
        if node not in visited:
            current = node
            visited.add(current)
            path.append(current)
            t_cost+=cost
        count +=1
    return path, t_cost
def Hill(graph, start, goal):
    best = 10000
    for i in range(1000):
        p, c = soln(graph, start, goal)
        if c<best:
            print(p)
            print(c)
            best = c
Hill(graph,start, goal)
