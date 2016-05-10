#! /usr/bin/env python3
import sys
def sort(data, debug=False):
    def merge(a, b):
        c = []
        a_pos, b_pos = 0, 0
        a_len, b_len = len(a), len(b)
        while a_pos < a_len or b_pos < b_len:
            if debug:
                print('c %s' % c)
                print('a %s: %d' % (a, a_pos))
                print('b %s: %d' % (b, b_pos))
            if b_pos >= b_len: 
                c.append(a[a_pos])
                a_pos += 1
                continue
            if a_pos >= a_len:
                c.append(b[b_pos])
                b_pos += 1
                continue
            if a[a_pos] < b[b_pos]:
                c.append(a[a_pos])
                a_pos += 1
            else:
                c.append(b[b_pos])
                b_pos += 1
        if debug:
            print("post-merge: %s" % c)
        return c

    def msort(data):
        if debug:
            print(data)
        if len(data) == 1:
            return data
        else:
            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]
            if debug:
                print(left, right)
            merged = merge(msort(left),msort(right))
            if debug:
                print("merged: %s" % merged)
            return merged

    return msort(data)

if __name__ == '__main__':
    import sys
    import random
    debug = True if len(sys.argv) > 2 and sys.argv[2] == 'debug' else False
    data = [random.randint(0,100) for i in range(int(sys.argv[1]))]

    print(data)
    print(sort(data))
    print(sort(data) == sorted(data))
