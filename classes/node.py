import random
import numpy as np

random.seed(244828)


class Node:
    def __init__(self, _id):
        self._id = _id
        self.location = None
        self.neigbours = []

    def show_node(self):
        print(self._id, self.location, self.neigbours)

    def get_location(self):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        z = random.randint(0, 50)
        self.location = np.asarray([x, y, z])

    def get_neighbours(self, _id, n_city, possible_roads):
        cities = [x for x in range(n_city)]
        cities.remove(_id)
        for neigbour in cities:
            if possible_roads[0] == 0:
                cities.remove(neigbour)
                possible_roads.remove(possible_roads[0])
            else:
                possible_roads.remove(possible_roads[0])
        cities_dic = {neighbour: None for neighbour in cities}
        self.neigbours = cities_dic
