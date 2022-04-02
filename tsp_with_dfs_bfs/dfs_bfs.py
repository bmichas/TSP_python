from copy import copy
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


def bfs_search(city_map: list[Node], start_point, city_count):
    path_lst, visited_lst = list(), list()
    for neighbor in city_map[start_point].neighbors:
        lst = [start_point, neighbor]
        path_lst.append(lst)
        visited_lst.append(lst)

    # print('Path:', path_lst)
    # print('Visited:', visited_lst)

    for i in range(city_count - 2):
        # print('====')
        for j in range(len(path_lst)):
            # print('----')
            path = path_lst[0]
            visited = visited_lst[0]
            start_point = path[-1]
            for neighbor in city_map[start_point].neighbors:
                if neighbor in visited:
                    # print('Already visited this city!')
                    pass
                else:
                    # print('Before:', path_lst)
                    new_path = copy(path)
                    new_path.append(neighbor)
                    path_lst.append(new_path)
                    visited_lst.append(new_path)
                    # print('After:', path_lst)
            path_lst.pop(0)
            visited_lst.pop(0)

    print('Path:', path_lst)
    print('Visited:', visited_lst)
