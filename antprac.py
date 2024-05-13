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
pheromone = {
    'S': [['A', 1], ['G', 1/10]],
    'A': [['B', 1/2], ['C', 1/1]],
    'B': [['D', 1/5]],
    'C': [['D', 1/3], ['G', 1/4]],
    'D': [['G', 1/2]],
    'G': []
}
def select_node(current_node, pheromone):
    neighbours = pheromone[current_node]
    nodes = []
    probablity = []
    for n, c in neighbours:
        nodes.append(n)
        probablity.append(c)
    selected_node = random.choices(nodes, weights=probablity)
    return selected_node[0]
def cal_cost(path, graph):
    cost = 0
    for i in range(0, len(path)-1,1):
        current = path[i]
        next = path[i+1]
        for n, c in graph[current]:
            if n == next:
                cost+=c
    return cost
def Ant(graph, start, goal):
    ants = 100
    best = 1000
    for i in range(ants):
        path = [start]
        current_node = start
        while(current_node!=goal):
            next = select_node(current_node, pheromone)
            path.append(next)
            current_node = next
        current_cost = cal_cost(path, graph)
        if current_cost<best:
            print(path)
            print(f"Cost: {current_cost}")
            best = current_cost
Ant(graph, start, goal)