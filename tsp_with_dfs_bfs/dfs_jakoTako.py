
def dfs_search(city_map: list[Node], start_point, city_count, path_lst=None):
    # Działa tylko dla 4 miast z wieksza ioscia ma problemy....

    if path_lst is None:
        city_map_original = city_map.copy()
        path_lst = []

    if len(city_map[start_point].neighbors) == 0:
        print("asdfasdfas", path_lst)
        return 2

    possible = list((city_map[start_point].neighbors).keys())
    city_map[start_point].neighbors.pop(possible[0])
    path_f = [start_point, possible[0]]
    alternative = list((city_map[path_f[-1]].neighbors).keys())

    for city in alternative:
        if city in path_f:
            alternative.remove(city)
    print(alternative)
    for city in alternative:
        visited = []
        print('kkkk', city)
        path = path_f.copy()
        if city not in path:
            path.append(city)
        possible = list((city_map[path[-1]].neighbors).keys())
        for k in range(city_count - 2):
            for i in possible:
                if i in path:
                    visited.append(i)
            for i in visited:
                if i in possible:
                    possible.remove(i)
            if len(possible) != 0:
                path.append(possible[0])
        if len(path) == city_count:
            path_lst.append(path)
        print('yeeeeeee', path)

    print(path_lst)
    dfs_search(city_map, start_point, city_count, path_lst)
