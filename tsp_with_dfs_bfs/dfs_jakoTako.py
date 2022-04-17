
def dfs_search(city_map: list[Node], start_point, city_count, visited=None):
    if visited is None:
        visited = []
        city_map_original = city_map.copy()

    visited = []
    if len(city_map[start_point].neighbors) == 0:
        return 2

    possible = list((city_map[start_point].neighbors).keys())
    city_map[start_point].neighbors.pop(possible[0])
    path = [start_point, possible[0]]
    alternative = list((city_map[path[-1]].neighbors).keys())

    #
    # Tutaj dodaj alterantywne trasy dodatkowa pętla
    #

    for k in range(city_count - 2):
        possible = list((city_map[path[-1]].neighbors).keys())
        for i in possible:
            if i in path:
                visited.append(i)
        for i in visited:
            if i in possible:
                possible.remove(i)
        path.append(possible[0])

    print(path)
    dfs_search(city_map, start_point, city_count, visited)
