import numpy as np
import csv_manager as csv
from random import *


def get_a_test_set(p):
    # P es el porcentaje que se desea tener en el dataset.
    test_set = []
    data_set = []
    [user, id, stars, _] = csv.read_data('../data/data_set.csv')
    i = 0
    while i < len(user):
        if random() > p:
            data_set.append([user, id, stars])
        else:
            test_set.append([user, id, stars])
        i += 1

    return test_set, data_set

[user, id, stars, unix_time] = csv.read_data('../data/data_set.csv')

np.save('../arrays/user_data.npy', user)
np.save('../arrays/id_data.npy', id)
np.save('../arrays/stars_data.npy', stars)
np.save('../arrays/unix_time_data.npy', unix_time)


[user_p, stars_p, unix_time_p] = csv.read_test('../data/a_puntuar.csv')

np.save('../arrays/user_puntuar.npy', user_p)
np.save('../arrays/stars_puntuar.npy', stars_p)
np.save('../arrays/unix_time_puntuar.npy', unix_time_p)

data, test = get_a_test_set(0.8)
