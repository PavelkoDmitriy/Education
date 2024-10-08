from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    # filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    t = datetime.now()
    """read_info(filenames[0])
    read_info(filenames[1])
    read_info(filenames[2])
    read_info(filenames[3])"""
    for n in filenames:
        read_info(n)
    print(datetime.now() - t)

    start_time = datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print(datetime.now() - start_time)
