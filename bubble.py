#! /usr/bin/env python3.6
from runner import run_sort_test

def bubble_sort(a):
    while True:
        for i, _ in enumerate(a[:-1]):
            if a[i+1] < a[i]:
                a[i], a[i+1] = a[i+1], a[i]
                break
        else:
            break


if __name__ == '__main__':
    run_sort_test(bubble_sort)
