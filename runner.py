import sys
import random

def run_sort_test(sort_fn):
    data = [random.randint(0,2**32) for i in range(int(sys.argv[1]))]

    print('Random data:')
    print(data)
    sort_fn(data)
    print('Sorted data:')
    print(data)
    print(f"Sort worked correctly: {data == sorted(data)}")
