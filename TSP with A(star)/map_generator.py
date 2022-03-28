from ast import If
import random
import numpy as np
import matplotlib.pyplot as plt

n_city = 4
start_point = 0
simetrical = False
roads = 0.8
possible_roads = [0]*round(n_city*(n_city - 1) * (1 - roads)) + \
    [1]*round(n_city*(n_city - 1) * roads)
random.shuffle(possible_roads)


class Node:
    def __init__(self, _id):
        self._id = _id
        self.location = None
        self.neighbors = []

    def show_node(self):
        print(self._id, self.location, self.neighbors)

    def get_location(self):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        z = random.randint(0, 50)
        self.location = np.asarray([x, y, z])

    def get_neighbors(self, _id):
        cities = [x for x in range(n_city)]
        cities.remove(_id)
        for neighbor in cities:
            if possible_roads[0] == 0:
                cities.remove(neighbor)
                possible_roads.remove(possible_roads[0])
            else:
                possible_roads.remove(possible_roads[0])
        cities_dic = {neighbor: None for neighbor in cities}
        self.neighbors = cities_dic


def aStar(city_map, visited=None, stack=None, cost=None, previous=None):
    if visited == None:
        visited = [start_point]
        cost = 0
        stack = city_map[start_point].neighbors

    minimum = float('inf')
    for i in stack:
        if minimum > stack[i]:
            minimum = stack[i]
            minimum_id = i
    print(minimum_id, minimum)


def count_cost(city_map):
    for start_city in city_map:
        start_node = start_city.location
        for neighbor in start_city.neighbors:
            end_node = city_map[neighbor].location
            dist = np.linalg.norm(start_node - end_node)
            if simetrical:
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
    city_map = []
    for city in range(n_city):
        node = Node(city)
        node.get_location()
        node.get_neighbors(city)
        city_map.append(node)

    city_map = count_cost(city_map)
    for city in city_map:
        city.show_node()

    shortest_path = aStar(city_map)
    # shortest_path = [0, 1, 2, 3, 0]
    # plot_results([city_map[int(i)].location for i in shortest_path])


if __name__ == "__main__":
    main()
