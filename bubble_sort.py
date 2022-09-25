# -*- coding: utf-8 -*-
# Bubble Sort Algorithm Implementation

def bubble_sort(arr):
     
    n = len(arr) 
    
    for i in range(n):
        for j in range(0, n-i-1):
            print(arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    print(arr)
                