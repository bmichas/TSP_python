import numpy as np
import matplotlib.pyplot as plt
from tsp_with_dfs_bfs.dfs_bfs import dfs_search, bfs_search, validShortestPath
from classes.node import Node
from global_parameters import *
from tsp_with_greed.greed import greed1, greed2, real_cost
from tsp_with_aStar.aStar import aStar
from tsp_with_aoc.aoc import Aoc
from timeit import default_timer as timer
import sys

"""
!TO DO!
- Genrator 1/1
- DFS 1/1
- BFS 1/1
- Greed 2/2
- A* 2/2
- AOC 0/1   
"""


def count_cost(city_map):
    for start_city in city_map:
        start_node = start_city.location
        for neighbor in start_city.neighbors:
            end_node = city_map[neighbor].location
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
            start_city.neighbors[neighbor] = dist
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
        node.get_neighbors(city, N_CITY, POSSIBLE_ROADS)
        city_map.append(node)

    city_map = count_cost(city_map)

    city_roads = {}
    for city in city_map:
        # city.show_node()
        city_roads[city._id] = city.neighbors

    """
    ########### DFS && BFS ########### 
    """
    # start = timer()
    # paths_dfs = dfs_search(city_map, START_POINT)
    # shortest_path_dfs, min_cost_dfs = validShortestPath(paths_dfs, city_map)
    # end = timer()
    # time_dfs = end - start

    # start = timer()
    # paths_bfs = bfs_search(city_map, START_POINT, N_CITY)
    # shortest_path_bfs, min_cost_bfs = validShortestPath(paths_bfs, city_map)
    # end = timer()
    # time_bfs = end - start
    
    # print(
    #     f'Schortest path DFS: {shortest_path_dfs}, Cost: {min_cost_dfs}, Execution time: {time_dfs}')
    # print(
    #     f'Schortest path BFS: {shortest_path_bfs}, Cost: {min_cost_bfs}, Execution time: {time_bfs}')

    """
    ############# GREED ##############
    """
    # start = timer()
    # shortest_path_greed1, cost_greed_1 = greed1(city_roads, START_POINT)
    # shortest_path_greed1, cost_greed_1 = real_cost(
    #     shortest_path_greed1, city_roads, cost_greed_1, N_CITY)
    # end = timer()
    # time_greed1 = end - start

    # start = timer()
    # shortest_path_greed2, cost_greed_2 = greed2(city_roads, START_POINT)
    # shortest_path_greed2, cost_greed_2 = real_cost(
    #     shortest_path_greed2, city_roads, cost_greed_2, N_CITY)
    # end = timer()
    # time_greed2 = end - start


    # print(
    #     f'Schortest path greed 1: {shortest_path_greed1}, Cost: {cost_greed_1}, Execution time: {time_greed1}')
    # print(
    #     f'Schortest path greed 2: {shortest_path_greed2}, Cost: {cost_greed_2}, Execution time: {time_greed2}')

    """
    ############# aStar, HEURISTICS: MEAN, MIN ##############
    # """
    # start = timer()
    # aStar_min = aStar(city_map, START_POINT, 'MIN')
    # aStar_min.get_path(START_POINT)
    # end = timer()
    # time_aStar_min = end - start

    # start = timer()
    # aStar_mean = aStar(city_map, START_POINT, 'MEAN')
    # aStar_mean.get_path(START_POINT)
    # end = timer()
    # time_aStar_mean = end - start

    # print(
    #     f'Schortest path A*(min): {aStar_min.current_path}, Cost: {aStar_min.cost}, Execution time: {time_aStar_min}')
    # print(
    #     f'Schortest path A*(mean): {aStar_mean.current_path}, Cost: {aStar_mean.cost}, Execution time: {time_aStar_mean}')
        
    """
    ############# AOC ##############
    """

    shortest_path_AOC = Aoc(city_map, START_POINT, 10)
    test = shortest_path_AOC.get_path(START_POINT)
    print(test)
    """
    ############# Vis ##############
    """
    # shortest_path_greed1 = [x for x in range(N_CITY)]
    # shortest_path_greed1.append(START_POINT)
    # plot_results([city_map[int(i)].location for i in shortest_path_greed1])


if __name__ == "__main__":
    main()
