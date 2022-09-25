# -*- coding: utf-8 -*-
# Selection Sort algorithm in Python
def selectionSort(arr):
     
    n = len(arr)
    
    for s in range(n):
        print(arr)
        min_idx = s
         
        for i in range(s + 1, n):
            if arr[i] < arr[min_idx]:
                min_idx = i
 
        arr[s], arr[min_idx] = arr[min_idx], arr[s]
        
    print(arr)
    return None
 
# Example to test the above code
arr = [2, 1, 10, 23, 0, 200, 4, 6, 3]
selectionSort(arr)