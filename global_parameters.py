import random



N_CITY = 5
START_POINT = 0
SYMMETRICAL = False
ROADS = 0.8
POSSIBLE_ROADS = [0]*round(N_CITY*(N_CITY - 1) * (1 - ROADS)) + \
    [1]*round(N_CITY*(N_CITY - 1) * ROADS)
random.shuffle(POSSIBLE_ROADS)
