# -*- coding: utf-8 -*-
# Bubble Sort Algorithm Implementation
def bubbleSort(arr):
     
    n = len(arr) 
    
    for i in range(n):
        for j in range(0, n-i-1):
            print(arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    print(arr)
    return None
                 
# Example to test the above code
arr = [2, 1, 10, 23, 0, 200, 4, 6, 3]
bubbleSort(arr)
 