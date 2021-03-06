import csv
import numpy as np


def read_csv(s):
    # Devuelve una matriz 2D donde cada fila corresponde a un usuario y cada película corresponde a una película
    # En la celda correspondiende aparece la puntuación de 1 a 5 o 0 si no está puntuada.
    x = np.zeros((943, 1682)).astype(int)    # I kind of cheat because I know the number
    with open(s) as dataset:
        reader = csv.reader(dataset)
        for row in reader:
            x[int(row[0]) - 1][int(row[1]) - 1] = int(row[2])
    return x


def read_data(s):
    # Use this to read the data_set.
    # It returns 4 arrays with the data
    with open(s) as dataset:
        # first_read = csv.reader(dataset)
        row_count = sum(1 for row in dataset)

    user = np.zeros(row_count).astype(int)
    id = np.zeros(row_count).astype(int)
    stars = np.zeros(row_count).astype(int)
    unix_time = np.zeros(row_count).astype(int)
    with open(s) as dataset:
        reader = csv.reader(dataset)
        count = 0
        for row in reader:
            user[count] = int(row[0])
            id[count] = int(row[1])
            stars[count] = int(row[2])
            unix_time[count] = int(row[3])
            count += 1

    return [user, id, stars, unix_time]


def read_test(s):
    # Same as read_data but for the a_puntuar csv.
    with open(s) as dataset:
        # first_read = csv.reader(dataset)
        row_count = sum(1 for row in dataset)

    user = np.zeros(row_count).astype(int)
    id = np.zeros(row_count).astype(int)
    unix_time = np.zeros(row_count).astype(int)
    with open(s) as dataset:
        reader = csv.reader(dataset)
        count = 0
        for row in reader:
            user[count] = int(row[0])
            id[count] = int(row[1])
            unix_time[count] = int(row[2])
            count += 1

    return [user, id, unix_time]


def convert_people(user, id, stars):
    # Convierte la información que devuelve read_data en una matríz de 3 dimensiones.
    # donde cada fila corresponde a un usuario y cada película corresponde a una película
    # la 3ra dimensión tiene longitud 5 y hay un 1 solo en el lugar correspondiente a la puntuación dada.
    num_users = int(max(user) - min(user) + 1)
    num_ids = int(max(id) - min(id) + 1)
    x = [[[0 for k in range(0, 5)] for i in range(0, num_ids)] for j in range(0, num_users)]
    x = np.array(x)
    for it in range(0, len(user)):
        x[int(user[it] - min(user))][int(id[it] - min(id))][int(stars[it] - 1)] = 1
    return x


def write_csv(s, user, id, stars, unix_time):
    with open(s, 'w') as answerset:
        rows = zip(user, id, stars, unix_time)
        writer = csv.writer(answerset)
        for row in rows:
            writer.writerow(row)
