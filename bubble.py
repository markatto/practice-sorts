#! /usr/bin/env python3

def sort(data, debug=False):
    i = 0
    while i < len(data) - 1:
        if(debug):
            print(i)
            print(data)
        if data[i] > data[i + 1]:
            tmp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = tmp
            i = 0
            continue
        i += 1


if __name__ == '__main__':
    import sys
    import random
    debug = True if len(sys.argv) > 2 and sys.argv[2] == 'debug' else False
    data = [random.randint(0,100) for i in range(int(sys.argv[1]))]

    print(data)
    sort(data, debug)
    print(data)
