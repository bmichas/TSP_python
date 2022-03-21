from tracemalloc import start


start_point = 0
all_paths = {0: [1, 2, 3],
             1: [0, 2, 3],
             2: [0, 1, 3],
             3: [0, 1, 2]}


def BFS(start_point,  all_paths, visited=None):
    if visited == None:
        visited = []
    city_paths = all_paths[start_point]
    for destination in city_paths:
        print(destination)
        visited.append([start_point, destination])
    print(visited)


BFS(start_point, all_paths)
