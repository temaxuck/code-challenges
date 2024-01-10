"""
    Heap - data structure, which is ordered binary tree.
    
    It is almost complete binary tree, except leaves are not necessary
    on the same level, but they are at max at 1 height apart. 
    
    Heap can be of two types:
        - max-heap - heap, where child is always less or equal to it's parent.
        - min-heap - heap, where child is always greater or equal to it's parent.

    Heap can be represented in array (or list). 
    Formulas to find left and right child of the node at index i are:
        - left child: i * 2 (or if indexing starts with 0: i * 2 + 1).
        - right child: i * 2 + 1 (or if indexing starts with 0: i * 2 + 2).
    Formula to find parent of the child at index i is: 
        - floor(i / 2).
        - floor((i + 1) / 2) (if indexing starts with 0).
    Formula to find leaves of the heap:
        - from n // 2 + 1 to n.
        - from n // 2 to n - 1 (if indexing starts with 0).
        
    Heap methods:
        - `heapify(a, heap_size, index)`, where `a` - initial data, 
          `heap_size` - size (length) of the `a`, `index` - index at which
          we are going to convert a to heap. `heapify` expects that children
          of the node at `index` are already heaps.
        - `build_heap(a)`, where `a` - initial data. `build_heap` is calls
          `heapify` for parents of each leaves-pair of the `a` since leaves are already heaps.   
"""
from enum import Enum
import operator as op
import math


class HEAP_TYPE(Enum):
    MAX_HEAP = 0
    MIN_HEAP = 1


def heapify(a, heap_size, i, heap_type=HEAP_TYPE.MAX_HEAP):
    operator = op.gt if heap_type == HEAP_TYPE.MAX_HEAP else op.lt

    l = i * 2 + 1
    r = i * 2 + 2
    largest = i

    if l < heap_size and operator(a[l], a[largest]):
        largest = l

    if r < heap_size and operator(a[r], a[largest]):
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, heap_size, largest, heap_type)


def build_heap(a, heap_type=HEAP_TYPE.MAX_HEAP):
    heap_size = len(a)
    parents = range(heap_size // 2 - 1, -1, -1)

    for i in parents:
        heapify(a, heap_size, i, heap_type)

    return a


def sort(a):
    a_copy = a[:]
    heap_size = len(a_copy)
    build_heap(a_copy)

    for i in range(heap_size - 1, 0, -1):
        a_copy[0], a_copy[i] = a_copy[i], a_copy[0]
        heapify(a_copy, i, 0)

    return a_copy


a = [2, 8, 5, 3, 9, 1]
print(sort(a), a)
