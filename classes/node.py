import random
import numpy as np

random.seed(244828)


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

    def get_neighbors(self, _id, n_city, possible_roads):
        cities = [x for x in range(n_city)]
        cities.remove(_id)
        for neighbor in cities:
            if possible_roads[0] == 0:
                cities.remove(neighbor)
                possible_roads.remove(possible_roads[0])
            else:
                possible_roads.remove(possible_roads[0])
        cities_dic = {neighbors: None for neighbors in cities}
        self.neighbors = cities_dic
