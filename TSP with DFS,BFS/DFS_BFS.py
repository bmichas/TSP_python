import numpy as np
import random
import math
import matplotlib.pyplot as plt
import collections

n_city = 4
start_point = 0
total = np.math.factorial(n_city - 1) / 2
roads = 0.8
simetrical = False


def calculate_cost(travel_cost, road):
    pass


def dfs(city_roads, start_point):
    print(city_roads)


def bfs(city_roads, start_point):
    print(city_roads)


def array_toDicts(travel_cost, n_city):
    raods_set = {}
    for i in range(n_city):
        road_set = {}
        for travel in travel_cost:
            if i == travel[0]:
                road_set[travel[1]] = travel[2]
        raods_set[i] = road_set
    return raods_set


def existing_rouds(travel_cost, possible_roads):
    lst = []
    for i in range(len(possible_roads)):
        road_status = possible_roads[i]
        if road_status == 0:
            lst.append(i)
        else:
            pass
    travel_cost = np.delete(travel_cost, lst, axis=0)
    return travel_cost


def count_distance(cities_location):
    travel_cost = []
    for i in range(len(cities_location)):
        for location in cities_location:
            result = np.where(cities_location == location)
            if i == result[0][0]:
                pass
            else:
                start = cities_location[i]
                dist = np.linalg.norm(start - location)
                if simetrical:
                    pass
                else:
                    if start[2] > location[2]:
                        dist = dist*0.9
                    elif start[2] < location[2]:
                        dist = dist*1.1
                    else:
                        dist = dist
                start = np.where(cities_location == cities_location[i])
                end = np.where(cities_location == location)
                travel_cost.append([start[0][0], end[0][0], dist])
    return np.asarray(travel_cost)


def gen_citi_location(n_city):
    coordinates = np.random.randint(-100, 100, size=(n_city, 2))
    height = np.random.randint(0, 50, size=(n_city, 1))
    return np.append(coordinates, height, axis=1)


def possible_roads_gen(n_city, roads):
    road_count = n_city*(n_city - 1)
    one_count = round(road_count * roads)
    zero_count = round(road_count - one_count)
    possible_roads = [0]*zero_count + [1]*one_count
    random.shuffle(possible_roads)
    return possible_roads


def plot_results(answer):
    x = [i[0] for i in answer]
    y = [i[1] for i in answer]
    z = [i[2] for i in answer]

    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    ax.scatter(x, y, z, c='black', s=100)
    ax.plot(x, y, z, color='red')
    plt.show()


def main():
    possible_roads = possible_roads_gen(n_city, roads)
    cities_location = gen_citi_location(n_city)
    travel_cost = count_distance(cities_location)
    travel_cost = existing_rouds(travel_cost, possible_roads)
    city_roads = array_toDicts(travel_cost, n_city)

    # city_connection_dfs = dfs(city_roads_set, start_point)
    # city_connection_bfs = bfs(city_roads, start_point)

    # roads_bfs = [[0, 1, 2, 3], [0, 1, 3, 2]]
    # roads_dfs = [[0, 1, 2, 3], [0, 1, 3, 2]]
    # shortest_path = [0, 1, 2, 3, 0]
    # journey_cost_bfs = []
    # journey_cost_dfs = []
    # for road in roads_bfs:
    #     travel_price = calculate_cost(travel_cost, road)
    #     journey_cost_bfs.append(travel_price)
    # for road in roads_dfs:
    #     travel_price = calculate_cost(travel_cost, road)
    #     journey_cost_dfs.append(travel_price)

    # plot_results([cities_location[i] for i in shortest_path])
    # print(roads)
    # print(travel_cost)


if __name__ == '__main__':
    main()
