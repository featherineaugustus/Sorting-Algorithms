# -*- coding: utf-8 -*-
# Quick Sort Algorithm Implementation
 
def partition(arr, l, r):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = arr[r], l
    for i in range(l, r):
        if arr[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            arr[i], arr[ptr] = arr[ptr], arr[i]
            print(arr)
            
            ptr += 1
            
    # Finally swapping the last element with the pointer indexed number
    arr[ptr], arr[r] = arr[r], arr[ptr]
    print(arr)
    
    return ptr
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
 
def quick_sort(arr, l, r):
    print(arr)
    if len(arr) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return arr
    if l < r:
        pi = partition(arr, l, r)
        quick_sort(arr, l, pi-1)  # Recursively sorting the left values
        quick_sort(arr, pi+1, r)  # Recursively sorting the right values
    return arr
 