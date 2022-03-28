from classes.node import Node

def getList(dict):
    return list(dict.keys())


def dfs_search(city_map: list[Node], start_point, visited=None, alternative=None):
    print(city_map[0].neighbors)

    if visited == None:
        visited = [start_point]

    neighbors = city_map[start_point].neighbors
    neighbors = getList(neighbors)
    alternative = neighbors
    if len(neighbors) == 0:
        print('brak somsiadow')

    start_point = neighbors[0]
    visited.append(start_point)
    alternative.remove(start_point)
    print(start_point)
    print(neighbors)
    print(visited)
    print(alternative)
