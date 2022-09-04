from typing import Counter
from classes.node import Node

class Aoc:
    def __init__(self, city_map: list[Node], start_point: int, ants: int) -> None:
        self.city_map = city_map
        self.start_point = start_point
        self.ants = ants
        self.pheromon_map = self._gen_pheromon_map()
        self.possible_paths = []
        self.current_path = []
        


    def _gen_pheromon_map(self):
        pheronom_map = []
        for city in self.city_map:
            pheromon_paths = {}
            for path in city.neighbors:
                pheromon_paths[path] = 1 / city.neighbors[path]
            pheronom_map.append(pheromon_paths)
        return pheronom_map
        
    def _check_valid_path(self):
        pass

    def _probability_of_path():
        pass

    def get_path(self, start_point, counter = 0):
        if counter == self.ants:
            print('Koniec roju')
            return 0 

        path = self.pheromon_map[self.start_point]

        """Ogarnąć zachowanie roju mrówek, dodać dodawnaie do trasy gdy przejdzie jakis odcinek sprawdzanie walidacji trasy"""

        counter += 1
        return self.get_path(start_point, counter)
