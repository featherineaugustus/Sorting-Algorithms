# -*- coding: utf-8 -*-
# Merge Sort algorithm in Python
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
        R = arr[mid:]
 
        # Merge sort
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    print(arr)
    return None

# Driver Code
if __name__ == '__main__':
    # Example to test the above code
    arr = [2, 1, 10, 23, 0, 200, 4, 6, 3]
    mergeSort(arr)