from classes.node import Node
import random
import sys
sys.setrecursionlimit(1000000000)

class Aoc:
    def __init__(self, city_map: list[Node], start_point: int, ants: int) -> None:
        self.start_point = start_point
        self.ants = ants
        self.city_map = self._get_city_map(city_map)
        self.pheromon_map = self._get_pheromon_map(city_map)
        self.best_path = []
        self.best_cost = float('inf')
        self.current_path = []
        

    def _get_city_map(self, city_map: list[Node]):
        new_city_map = []
        for city in city_map:
            new_city_map.append(city.neighbors)

        return new_city_map


    def _get_pheromon_map(self, city_map: list):
        pheronom_map = []
        for city in city_map:
            pheromon_paths = {}
            for path in city.neighbors:
                pheromon_paths[path] = 1
            pheronom_map.append(pheromon_paths)

        return pheronom_map
        

    def _weighted_random_choice(self, choices):
        max = sum(choices.values())
        pick = random.uniform(0, max)
        current = 0
        for key, value in choices.items():
            current += value
            if current > pick:
                return key


    def _probability_of_path(self, paths: dict, pheromon_paths: dict ):
        probability_of_path = {}
        for path in paths:
            nominator = pheromon_paths[path] * 1 / paths[path]
            denominator = 0
            for pheromon_path in pheromon_paths:
                denominator += pheromon_paths[pheromon_path] * 1 / paths[pheromon_path]
            probability_of_path[path] = nominator/denominator

        return self._weighted_random_choice(probability_of_path)


    def _veporize(self):
        for path in self.pheromon_map:
            for point in path:
                path[point] *= 0.5


    def _add_pheromone_on_path(self):
        cost = 0
        for i in range(len(self.current_path) - 1):
            destiantions = self.city_map[self.current_path[i]]
            destiantion_cost = destiantions[self.current_path[i+1]]
            cost += destiantion_cost

        if cost < self.best_cost:
            self.best_cost = cost
            self.best_path = self.current_path

        pheromon = 1/cost
        for i in range(len(self.current_path) - 1):
            destiantions = self.pheromon_map[self.current_path[i]]
            destiantions[self.current_path[i+1]] += pheromon


    def _valid_path(self):
        last_point = self.current_path[-1]
        if 0 in list(self.city_map[last_point].keys()):
            self.current_path.append(0)
            self._veporize()
            self._add_pheromone_on_path()
            self.current_path = []
            self.ants -= 1
            return self.get_path(self.start_point)
    
        self.ants -= 1
        self.current_path = []
        return self.get_path(self.start_point)


    def get_path(self, start_point = 0):
        if self.ants == 0:
            return 0

        if len(self.current_path) == 0:
            self.current_path.append(start_point)

        if len(self.current_path) == len(self.city_map):
            self._valid_path()
    
        picked_destination = self._probability_of_path(self.city_map[start_point], self.pheromon_map[start_point])
        if picked_destination in self.current_path:
            return self.get_path(start_point)
        else:
            self.current_path.append(picked_destination)
            return self.get_path(picked_destination)
