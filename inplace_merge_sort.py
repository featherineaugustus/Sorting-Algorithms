# -*- coding: utf-8 -*-
# In-place Merge Sort Algorithm Implementation
  
def merge(arr, start, mid, end):
    start2 = mid + 1
  
    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return
  
    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):
  
        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
  
            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                print(arr)
                index -= 1
  
            arr[start] = value
            print(arr)
  
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
            
    
  
  
'''
* l is for left index and r is right index of
the sub-array of arr to be sorted
'''
  
  
def inplace_merge_sort(arr, l, r):
    if (l < r):
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
  
        # Sort first and second halves
        inplace_merge_sort(arr, l, m)
        inplace_merge_sort(arr, m + 1, r)
  
        merge(arr, l, m, r)