#! /usr/bin/env python3.6
from runner import run_sort_test

def selection_sort(a):
    for i, _ in enumerate(a):
        lowest = min(a[i:])
        lowest_index = a.index(lowest)
        tmp = a[i]
        a[i] = lowest
        a[lowest_index] = tmp



if __name__ == '__main__':
    run_sort_test(selection_sort)
