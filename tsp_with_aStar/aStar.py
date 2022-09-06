import copy
from classes.node import Node
import sys
sys.setrecursionlimit(10000)


class aStar:
    def __init__(self, city_map: list[Node], start_point, heuristic):
        self.city_map = city_map
        self.start_point = start_point
        self.cost = 0
        self.possible_paths = []
        self.current_path = []
        if heuristic == 'MIN':
            self._get_global_min()
        if heuristic == 'MEAN':
            self._get_global_mean()
        

    def _get_global_min(self):
        self.global_heuristic = float('inf')
        for city in self.city_map:
            lst = city.neighbors.values()
            if min(lst) < self.global_heuristic:
                self.global_heuristic = min(lst)

    def _get_global_mean(self):
        sum_dist = 0
        divider = 0
        for city in self.city_map:
            lst = city.neighbors.values()
            sum_dist += sum(lst)
            divider += len(lst)
        self.global_heuristic = sum_dist/divider

    def _cost(self, path):
        cost = 0
        if len(path) == 1:
            return 0

        for i in range(len(path)-1):
            cost += self.city_map[path[i]].neighbors[path[i+1]]
        return cost
        

    def get_path(self, start_point,path_to_remove = []):
        sys.setrecursionlimit(1950)
        if len(self.current_path) == len(self.city_map)+1:
            self.cost = self._cost(self.current_path)
            return 0

        if path_to_remove in self.possible_paths:
            self.possible_paths.remove(path_to_remove)

        if start_point == self.start_point:
            x = float('inf')
            self.current_path.append(start_point)
            self.possible_paths.append((self.current_path,x))
        
        heuristic_multiplicator = len(self.city_map) + 1 - len(self.current_path)
        for neighbour in self.city_map[start_point].neighbors:
            path = list(copy.copy(self.current_path))
            local_cost = self._cost(path)
            if neighbour != start_point and neighbour not in self.current_path:
                local_cost += self.city_map[start_point].neighbors[neighbour] + (self.global_heuristic * heuristic_multiplicator)
                path.append(neighbour)
                self.possible_paths.append((path,local_cost))
            if len(self.current_path) == len(self.city_map) and neighbour == 0:
                local_cost += self.city_map[start_point].neighbors[neighbour] + (self.global_heuristic * heuristic_multiplicator)
                path.append(neighbour)
                self.possible_paths.append((path,local_cost))

        path_to_remove = []
        min_local = float('inf')
        for path in self.possible_paths:
            if min_local > path[1]:
                min_local = path[1]
                self.current_path = path[0]
                path_to_remove = path

        new_start_point = self.current_path[-1]
        self.get_path(new_start_point, path_to_remove)
