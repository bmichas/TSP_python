# from ..classes.node import Node

from classes.node import Node

def getList(dict):
    return list(dict.keys())


def dfs_search(city_map: list[Node], start_point, visited=None, alternative=None):
    print(city_map.neighbours)

    if visited == None:
        visited = [start_point]

    neighbours = city_map[start_point].neighbours
    neighbours = getList(neighbours)
    alternative = neighbours
    if len(neighbours) == 0:
        print('brak somsiadow')

    start_point = neighbours[0]
    visited.append(start_point)
    alternative.remove(start_point)
    print(start_point)
    print(neighbours)
    print(visited)
    print(alternative)