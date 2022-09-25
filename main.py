# -*- coding: utf-8 -*-

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from inplace_merge_sort import inplace_merge_sort

if __name__ == '__main__':
    # Example to test the above code
    #arr = [9, 2, 8, 1, 10, 5, 7, 4, 6, 3]
    arr = [4,1,5,3,2]

    print('\nBubble Sort:')
    bubble_sort(arr.copy())
    
    print('\nSelection Sort:')
    selection_sort(arr.copy())
    
    print('\nInsertion Sort:')
    insertion_sort(arr.copy())
    
    print('\nQuick Sort:')
    quick_sort(arr.copy(), 0, len(arr)-1)
    
    print('\nMerge Sort:')
    merge_sort(arr.copy())
    
    print('\nHeap Sort:')
    heap_sort(arr.copy())
    
    print('\nIn-place Merge Sort:')
    inplace_merge_sort(arr.copy(), 0, len(arr)-1)
    
    
    
    
    
    
    