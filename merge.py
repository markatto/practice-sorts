#! /usr/bin/env python3.6
import sys
from heapq import merge
from runner import run_sort_test

def msort(data):
    '''do a merge sort'''
    if len(data) == 1:
        return data
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    merged = merge(msort(left),msort(right))
    return merged

def mergesort(data):
    '''make it look like msort runs in-place so the test harness works'''
    data[:] = msort(data)

if __name__ == '__main__':
    run_sort_test(mergesort)
