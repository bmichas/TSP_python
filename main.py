import numpy as np
import matplotlib.pyplot as plt
# from tsp_with_dfs_bfs.dfs_bfs import dfs_search
from classes.node import Node
from global_parameters import *
from tsp_with_greed.greed import greed1, greed2, real_cost

"""
!TO DO!
- Genrator 1/1
- DFS 0/1
- BFS 0/1
- Greed 2/2
- A* 0/2
- AOC 0/1   
"""


def count_cost(city_map):
    for start_city in city_map:
        start_node = start_city.location
        for neighbour in start_city.neigbours:
            end_node = city_map[neighbour].location
            dist = np.linalg.norm(start_node - end_node)
            if SYMMETRICAL:
                pass
            else:
                if start_node[2] > end_node[2]:
                    dist = dist*0.9
                elif start_node[2] < end_node[2]:
                    dist = dist*1.1
                else:
                    dist = dist
            start_city.neigbours[neighbour] = dist
    return city_map


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
    """
    ########### GENERATOR ############
    """

    city_map = []
    for city in range(N_CITY):
        node = Node(city)
        node.get_location()
        node.get_neighbours(city, N_CITY, POSSIBLE_ROADS)
        city_map.append(node)

    city_map = count_cost(city_map)

    city_roads = {}
    for city in city_map:
        city.show_node()
        city_roads[city._id] = city.neigbours

    """
    ########### DFS && BFS ########### 
    """

    # shortest_path_dfs = dfs_search(city_map, start_point)
    # shortest_path_bfs = bfs_serach()

    """
    ############# GREED ##############
    """

    print(city_roads)
    shortest_path_greed1, cost_greed_1 = greed1(city_roads, START_POINT)
    shortest_path_greed1, cost_greed_1 = real_cost(
        shortest_path_greed1, city_roads, cost_greed_1, N_CITY)
    shortest_path_greed2, cost_greed_2 = greed2(city_roads, START_POINT)
    shortest_path_greed2, cost_greed_2 = real_cost(
        shortest_path_greed2, city_roads, cost_greed_2, N_CITY)

    print(
        f'Schortest path greed 1: {shortest_path_greed1}, Cost: {cost_greed_1}')
    print(
        f'Schortest path greed 2: {shortest_path_greed2}, Cost: {cost_greed_2}')

    """
    ############# Astar ##############
    """

    # shortest_path_Astar1 = a_star1()
    # shortest_path_Astar2 = a_star2()
    """
    ############# AOC ##############
    """

    # shortest_path_AOC = aoc()

    """
    ############# Vis ##############
    """
    shortest_path_greed1 = [x for x in range(N_CITY)]
    shortest_path_greed1.append(START_POINT)
    plot_results([city_map[int(i)].location for i in shortest_path_greed1])


if __name__ == "__main__":
    main()
