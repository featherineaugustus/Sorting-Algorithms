# -*- coding: utf-8 -*-
# Selection Sort algorithm in Python

def selection_sort(arr):
     
    n = len(arr)
    
    for s in range(n):
        print(arr)
        min_idx = s
         
        for i in range(s + 1, n):
            if arr[i] < arr[min_idx]:
                min_idx = i
 
        arr[s], arr[min_idx] = arr[min_idx], arr[s]
        
    print(arr)