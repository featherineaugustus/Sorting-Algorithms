# -*- coding: utf-8 -*-
# Driver Code

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

if __name__ == '__main__':
    # Example to test the above code
    arr = [9, 2, 8, 1, 10, 5, 7, 4, 6, 3]
    
    print('\nBubble Sort:')
    bubble_sort(arr)
    
    print('\nSelection Sort:')
    selection_sort(arr)
    
    print('\nInsertion Sort:')
    insertion_sort(arr)
    
    print('\nMerge Sort:')
    merge_sort(arr)