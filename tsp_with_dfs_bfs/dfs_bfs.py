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


def bfs_search(city_map: list[Node], start_point, city_count, visited_lst=None, path_lst=None):
    if visited_lst == None:
        path_lst = list()
        visited_lst = list()
        for neighbor in city_map[start_point].neighbors:
            lst = [start_point, neighbor]
            path_lst.append(lst)
            visited_lst.append(lst)

    print('Path:', path_lst)
    print('Visited:', visited_lst)

    # tu jest cos nie tak nie idze dobrze po paths
    # tak samo jest cos nie tak z lista visited
    # ewaluacje pierwszej pętli powinny zostac tak jak są
    # ale kolejna pętla powinna prawdopodomnie być względem listy path
    for i in range(city_count - 1):
        print('====')
        path = path_lst[0]
        visited = visited_lst[0]
        start_point = path[-1]
        for neighbor in city_map[start_point].neighbors:
            if neighbor in visited:
                print('jest ten somsiad')
            else:
                print('przed', path_lst)
                new_path = copy(path)
                new_path.append(neighbor)
                path_lst.append(new_path)
                visited_lst.append(new_path)
                print('po', path_lst)
        path_lst.pop(0)
        visited_lst.pop(0)

    print('Path:', path_lst)
    print('Visited:', visited_lst)
