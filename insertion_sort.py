# -*- coding: utf-8 -*-
# Insertion Sort algorithm in Python

def insertion_sort(arr): 
   
   for i in range(1, len(arr)): 
       print(arr)    
   
       a = arr[i] 
       j = i - 1 
       
       while j >= 0 and a < arr[j]: 
           arr[j + 1] = arr[j] 
           j -= 1 
             
       arr[j + 1] = a 
         
   print(arr)
        