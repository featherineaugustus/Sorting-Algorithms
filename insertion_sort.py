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
   return None 
            
# Driver Code
if __name__ == '__main__':
    # Example to test the above code
    arr = [2, 1, 10, 23, 0, 200, 4, 6, 3]
    insertion_sort(arr)