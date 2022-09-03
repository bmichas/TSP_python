from classes.node import Node
import numpy as np


class aStar:
    def __init__(self, city_map: list[Node], start_point):
        self.cityMap = city_map
        self.startPoint = start_point
        self.currentPathCost = int  # int
        self.paths = dict  # dict
        self.global_min = self._get_global_min()  # int
        self.currentPath = list  # list

    def _get_global_min(self):
        min_dist = float('inf')
        for city in self.cityMap:
            lst = city.neighbors.values()
            if min(lst) < min_dist:
                min_dist = min(lst)
        self.global_min = min_dist
    

    def _heuristic(self):
        pass

    def _get_path(self):
        pass
        # while len(self.currentPath) != len(self.cityMap) + 1:
        #     pass
