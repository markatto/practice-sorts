#! /usr/bin/env python3.6
from runner import run_sort_test

def selection_sort(a):
    for i, _ in enumerate(a):
        lowest_index = a.index(min(a[i:]))
        a[lowest_index], a[i] = a[i], a[lowest_index]



if __name__ == '__main__':
    run_sort_test(selection_sort)
