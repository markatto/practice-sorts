#! /usr/bin/env python3.6
import sys
from runner import run_sort_test

def merge(a, b):
    '''merge two sorted lists'''
    c = []
    a_pos, b_pos = 0, 0
    a_len, b_len = len(a), len(b)
    while a_pos < a_len or b_pos < b_len:
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
    return c


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
