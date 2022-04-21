from copy import copy
from hashlib import new
from classes.node import Node


def getList(dict):
    return list(dict.keys())


def validShortestPath(path_lst, city_map: list[Node]):
    valid_paths, travel_cost_lst = list(), list()
    for path in path_lst:
        start_point = path[-1]
        end_point = path[0]
        cities = getList(city_map[start_point].neighbors)
        if end_point in cities:
            path.append(end_point)
            valid_paths.append(path)
            travel_cost = 0
            for i in range(len(path) - 1):

                cost = city_map[path[i]].neighbors[path[i + 1]]
                travel_cost += cost
            travel_cost_lst.append(travel_cost)

    min_cost_index = travel_cost_lst.index(min(travel_cost_lst))

    return valid_paths[min_cost_index], travel_cost_lst[min_cost_index]


def dfs_search(city_map: list[Node], start_point, path=None, path_lst=list()):
    if path is None:
        path = [start_point]

    if len(path) == len(city_map):
        path_lst.append(path)

    possible = getList(city_map[start_point].neighbors)
    for i in possible:
        if i not in path:
            new_path = path.copy()
            new_path.append(i)
            dfs_search(city_map, i, new_path, path_lst)

    return path_lst


def bfs_search(city_map: list[Node], start_point, city_count):
    path_lst, visited_lst = list(), list()
    for neighbor in city_map[start_point].neighbors:
        lst = [start_point, neighbor]
        path_lst.append(lst)
        visited_lst.append(lst)

    for i in range(city_count - 2):
        for j in range(len(path_lst)):
            path = path_lst[0]
            visited = visited_lst[0]
            start_point = path[-1]
            for neighbor in city_map[start_point].neighbors:
                if neighbor in visited:
                    pass
                else:
                    new_path = copy(path)
                    new_path.append(neighbor)
                    path_lst.append(new_path)
                    visited_lst.append(new_path)
            path_lst.pop(0)
            visited_lst.pop(0)

    return path_lst
