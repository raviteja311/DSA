def bubble_sort(arr):
    '''
    function to perform the bubble_sort 
    parameter arr :List to search 
    '''
    n = len(arr)                                  #length of the array is assigned to n
    
    for  i in range(n):                           #Traverse through all the elements
        
        for j in range(n-i-1):                    #Last i elements are already sorted, so we don't need to check them 
            
            if arr[j] > arr[j+1]:                 #Swap if the element found is greater than the next element 
                
                arr[j],arr[j+1] = arr[j+1],arr[j] #swapping
                
    return arr

#Example
arr = [64,34,25,12,22,11,9]

#Display the original
print("Original_array : ",arr)

#calling the function
result = bubble_sort(arr)

#Display the sorted list
print("Sorted_array   :",result)