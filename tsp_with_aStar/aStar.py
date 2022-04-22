from typing_extensions import Self
from classes.node import Node


class aStar:
    def __init__(self, city_map: list[Node], start_point):
        self.cityMap = city_map
        self.startPoint = start_point
        self.currentPathCost = int  # int
        self.paths = dict  # dict
        self.globalMin = int  # int
        self.currentPath = list  # list

    def getGlobalMin(self):
        for city in self.cityMap:
            city

    def heuristic(self):
        pass

    def getPath(self):

        pass
        # while len(self.currentPath) != len(self.cityMap) + 1:
        #     pass
