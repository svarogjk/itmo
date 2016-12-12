import pickle

trains = []
filename = 'train.pickle'


def write_train(count, power, size):
    with open(filename, 'wb') as f:
        # trains += [
        #     (count, power, size)
        # ]
        trains.append((count, power, size))
        pickle.dump(trains, f)


# input('Число тепловозов'),
# input('Мощность'),
# input('Габариты')

def read_trains():
    with open(filename, 'rb') as f:
        trains = pickle.load(f)
    return trains

