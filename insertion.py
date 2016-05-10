#! /usr/bin/env python3

def sort(data, debug=False):
    pass

if __name__ == '__main__':
    import sys
    import random
    debug = True if len(sys.argv) > 2 and sys.argv[2] == 'debug' else False
    data = [random.randint(0,100) for i in range(int(sys.argv[1]))]

    print(data)
    sort(data, debug)
    print(data)
