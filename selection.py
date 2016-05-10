#! /usr/bin/env python3

def sort(data, debug=False):
    pass

def insert_sort(data):
    data = data[:]
    new = []
    while len(data) > 0:
        # find the min
        minimum = None
        min_index = None
        for index, item in enumerate(data):
            if index == 0:
                minimum = item
                min_index = index
                continue
            if item < minimum:
                minimum = item
                min_index = index
        del(data[min_index])
        new.append(minimum)
    return new



if __name__ == '__main__':
    import sys
    import random
    debug = True if len(sys.argv) > 2 and sys.argv[2] == 'debug' else False
    data = [random.randint(0,100) for i in range(int(sys.argv[1]))]

    print(data)
    print(insert_sort(data))
    print(sorted(data))
