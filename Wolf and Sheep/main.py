def read_graph():
    graph_dict = {}
    graph_file = open('graph.txt', 'r')
    lines = graph_file.readlines()
    for i, line in enumerate(lines):
        children = []
        connections = line.split()
        for j, connection in enumerate(connections):
            if connection == '1':
                children.append(j)
        graph_dict[i] = children
    return graph_dict


def remove_path(graph, path):
    while len(path)>1:
        j = path.pop()
        i = path[-1]
        graph[i].remove(j)
    return graph


def backtrack(parent_map, goal):
    path = []
    vertex = goal
    while (bool(parent_map.get(vertex))):
        path.append(int(vertex))
        vertex = parent_map[vertex]
    path.append(int(vertex))
    path.reverse()
    return path


def DFS(start, goal, graph):
    stack, visited, path = [start], [], []
    parent_map = {}
    path_found = False
    while stack:
        vertex = stack.pop()
        visited.append(vertex)
        if vertex == goal:
            path = backtrack(parent_map, str(goal))
            path_found = True
            break
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                parent_map[str(neighbor)] = str(vertex)
                stack.append(neighbor)
    return path_found, path


start = 0
finish = 5
graph_dict = read_graph()
sh_p_found, sheep_path = DFS(start, finish, graph_dict)
if sh_p_found:
    used_path = sheep_path.copy()
    graph_dict = remove_path(graph_dict, used_path)
    w_p_found, wolf_path = DFS(start, finish, graph_dict)
    if w_p_found:
        print(f'here are two paths:\n path for Sheep: {sheep_path}\n path for wolves: {wolf_path}')
    else:
        print('no path for wolves found :(')
else:
    print('no 2 paths found :(')
