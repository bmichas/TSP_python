import copy


def real_cost(best_path, city_roads_original, cost_original, n_city):
    city_roads = copy.deepcopy(city_roads_original)
    cost = copy.deepcopy(cost_original)
    start_city = best_path[-1]
    end_city = best_path[0]
    city_roads_last = city_roads[start_city]
    last_cost = city_roads_last.get(end_city)
    if last_cost == None:
        print('From this path you can not get to home location!')
        return best_path, cost
    cost += last_cost
    best_path.append(end_city)
    if len(best_path) == n_city + 1:
        return best_path, cost
    else:
        print('Path is not valid!')
        return best_path, cost


def greed1(city_roads_original, start_point, visited=None, cost=None):
    city_roads = copy.deepcopy(city_roads_original)
    if visited == None:
        visited = [start_point]
        cost = 0

    roads = city_roads[start_point]
    if not roads:
        return visited, cost
    min_cost = float("inf")
    for destination in roads:
        if city_roads[start_point][destination] < min_cost:
            min_cost = city_roads[start_point][destination]
            shortest_path = destination
    for city in city_roads:
        roads = city_roads[city]
        if start_point in roads:
            roads.pop(start_point)
        if shortest_path in roads:
            roads.pop(shortest_path)
        city_roads[city] = roads
    visited.append(shortest_path)
    cost += min_cost
    return greed1(city_roads, shortest_path, visited, cost)


def greed2(city_roads_original, start_point, visited=None, cost=None):
    city_roads = copy.deepcopy(city_roads_original)
    if visited == None:
        visited = [start_point]
        cost = 0

    roads = city_roads[start_point]
    if not roads:
        return visited, cost
    min_cost1 = min_cost2 = float("inf")
    for destination in roads:
        if city_roads[start_point][destination] <= min_cost1:
            min_cost1, min_cost2 = city_roads[start_point][destination], min_cost1
        elif city_roads[start_point][destination] < min_cost2:
            min_cost2 = city_roads[start_point][destination]
    for destination, cost_to in roads.items():
        if cost_to == min_cost2:
            shortest_path = destination
    for city in city_roads:
        roads = city_roads[city]
        if start_point in roads:
            roads.pop(start_point)
        if shortest_path in roads:
            roads.pop(shortest_path)
        city_roads[city] = roads
    visited.append(shortest_path)
    cost += min_cost2
    return greed1(city_roads, shortest_path, visited, cost)
