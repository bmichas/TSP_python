from msilib.schema import SelfReg
from tracemalloc import start
from classes.node import Node
import numpy as np


class aStar:
    def __init__(self, city_map: list[Node], start_point, heuristic):
        self.city_map = city_map
        self.start_point = start_point
        self.visited = []
        self.possible_paths = []
        self.current_path = []
        if heuristic == 'MIN':
            self._get_global_min()
        if heuristic == 'MEAN':
            self._get_global_mean()
        

    def _get_global_min(self):
        self.global_min = float('inf')
        for city in self.city_map:
            lst = city.neighbors.values()
            if min(lst) < self.global_min:
                self.global_min = min(lst)

    def _get_global_mean(self):
        sum_dist = 0
        divider = 0
        for city in self.city_map:
            lst = city.neighbors.values()
            sum_dist += sum(lst)
            divider += len(lst)
        self.global_mean = sum_dist/divider

    def _calculate_cost(self):
        pass

    def get_path(self, start_point):
        if start_point == self.start_point:
            self.visited.append((start_point,float('inf')))
            self.current_path.append(start_point)

        local_min = float('inf')
        for neighbour in self.city_map[start_point].neighbors:
            local_cost = self.city_map[start_point].neighbors[neighbour] + (self.global_min * 4)
            if local_min > local_cost:
                local_min = local_cost
                close_neighbour = neighbour

        self.current_path.append(close_neighbour)
        print(self.current_path)

    
             
                

# 0 [-24  69  45] {1: 128.07224523681936, 2: 67.31374302473455, 3: 165.9347160783421}
# 1 [-88 -56  22] {0: 156.53274417833478, 2: 102.27580359009652, 3: 50.30019880676418}
# 2 [-89  57  10] {0: 82.27235258578668, 1: 125.00375994345131, 3: 173.8034809777986}
# 3 [-99 -99  33] {0: 202.8090974290848, 1: 41.15470811462524, 2: 142.2028480727443}