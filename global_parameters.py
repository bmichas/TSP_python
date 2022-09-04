import random


N_CITY = 4
START_POINT = 0
SYMMETRICAL = False
ROADS = 1
POSSIBLE_ROADS = [0]*round(N_CITY*(N_CITY - 1) * (1 - ROADS)) + \
    [1]*round(N_CITY*(N_CITY - 1) * ROADS)
random.shuffle(POSSIBLE_ROADS)
