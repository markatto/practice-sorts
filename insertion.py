#! /usr/bin/env python3.6
from bisect import bisect_left
from runner import run_sort_test


def insertion_sort(a):
    for i in range(1, len(a)):
        insert_pos = bisect_left(a[:i], a[i])
        a[insert_pos:i+1] = [a[i]] + a[insert_pos:i]

if __name__ == '__main__':
    run_sort_test(insertion_sort)
